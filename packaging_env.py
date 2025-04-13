import gymnasium as gym
from gymnasium import spaces
import pybullet as p
import pybullet_data
import numpy as np
import time
import math

class PackagingFragilityEnv(gym.Env):
    metadata = {"render_modes": ["human"], "render_fps": 60}

    def __init__(self, render_mode=None):
        super(PackagingFragilityEnv, self).__init__()
        self.render_mode = render_mode
        self.client = p.connect(p.GUI if render_mode == "human" else p.DIRECT)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -10)

        # Step counter
        self.step_count = 0
        self.max_steps = 10_000  # ✅ MAX STEPS PER EPISODE

        # Define observation/action spaces
        obs_low = np.array([-np.pi]*7 + [0.0] + [-1]*3 + [-1]*3, dtype=np.float32)
        obs_high = np.array([np.pi]*7 + [0.06] + [1]*3 + [1]*3, dtype=np.float32)
        self.observation_space = spaces.Box(low=obs_low, high=obs_high, dtype=np.float32)
        self.action_space = spaces.Discrete(7)

        self.joint_indices = list(range(7))
        self.gripper_indices = [9, 10]
        self._load_env()


    def _load_env(self):
        self.plane = p.loadURDF("plane.urdf")
        self.table = p.loadURDF("table/table.urdf", basePosition=[0.5, 0, -0.65])
        self.tray = p.loadURDF("tray/traybox.urdf", basePosition=[0.5, 0, 0])
        self.object = p.loadURDF("random_urdfs/000/000.urdf", basePosition=[0.6, 0, 0.1])
        self.robot = p.loadURDF("franka_panda/panda.urdf", useFixedBase=True)

    def _get_obs(self):
        joint_states = [p.getJointState(self.robot, i)[0] for i in self.joint_indices]
        gripper_state = p.getJointState(self.robot, self.gripper_indices[0])[0]
        obj_pos, _ = p.getBasePositionAndOrientation(self.object)
        obj_vel, _ = p.getBaseVelocity(self.object)
        return np.array(joint_states + [gripper_state] + list(obj_pos) + list(obj_vel), dtype=np.float32)

    def _apply_action(self, action):
        poses = [
            [0, 0.6, 0, -1.2, 0, 1.5, -0.6],         # above object
            [0, 0.6, -0.2, -1.4, 0, 1.5, -0.6],      # grasp
            [0, 0.4, 0, -1.0, 0, 1.5, -0.6],         # lift
            [-0.5, 0.1, 0.3, -2.0, 0, 2.0, -0.8],    # closer above tray
            [-0.5, 0.1, 0.1, -2.2, 0, 2.2, -0.8],    # closer drop
        ]

        if action < 5:
            for i in range(7):
                p.setJointMotorControl2(self.robot, i, p.POSITION_CONTROL, poses[action][i])
        elif action == 5:
            self._control_gripper(open=False)
        elif action == 6:
            self._control_gripper(open=True)
        for _ in range(10):
            p.stepSimulation()

    def _control_gripper(self, open=True):
        target = 0.04 if open else 0.0
        for i in self.gripper_indices:
            p.setJointMotorControl2(self.robot, i, p.POSITION_CONTROL, target, force=10)

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.step_count = 0  # ✅ Reset step count
        p.resetSimulation()
        p.setGravity(0, 0, -10)
        self._load_env()
        self._control_gripper(open=True)
        for _ in range(50):
            p.stepSimulation()
        obs = self._get_obs()
        return obs, {}

    def step(self, action):
        self.step_count += 1  # ✅ Track episode length
        self._apply_action(action)
        obs = self._get_obs()
        obj_pos, _ = p.getBasePositionAndOrientation(self.object)

        # Track previous object position for change detection
        prev_obj_pos = getattr(self, "prev_obj_pos", None)
        self.prev_obj_pos = obj_pos  # Save for next step

        # Initialize reward and termination flags
        reward = 0.0
        terminated = False
        truncated = False

        # Calculate distance toward target x position
        target_x = 0.6
        height_threshold = 0.1

        # =========================
        # ✨ Step-wise Reward Logic
        # =========================

        # 1. Reward forward progress (toward tray)
        x_progress = obj_pos[0] / target_x
        x_progress = np.clip(x_progress, 0.0, 1.0)
        reward += x_progress * 2.0  # scaled reward for forward motion

        # 2. Reward lifting
        if obj_pos[2] > height_threshold:
            reward += 3.0

        # 3. Reward upward movement; penalize drops
        if prev_obj_pos:
            delta_z = obj_pos[2] - prev_obj_pos[2]
            if delta_z > 0.01:
                reward += 1.0
            elif delta_z < -0.01:
                reward -= 2.0

        # 4. Penalize inactivity / no movement
        if prev_obj_pos:
            delta = np.linalg.norm(np.array(obj_pos) - np.array(prev_obj_pos))
            if delta < 0.001:
                reward -= 1.0

        # 5. Terminal rewards / penalties
        if obj_pos[0] > target_x and obj_pos[2] > height_threshold:
            reward += 10.0
            terminated = True
        elif obj_pos[2] < 0.02:
            print("[INFO] Episode ended: Object dropped.")
            reward = -10.0
            terminated = True

        # ✅ Now it's safe to log
        print(f"Step {self.step_count}: action={action}, Reward: {reward:.2f}, Done: {terminated}, Truncated: {truncated}")
        return obs, reward, terminated, truncated, {}
        

    def render(self):
        # Only for GUI mode
        time.sleep(1. / 60.)

    def close(self):
        p.disconnect()
