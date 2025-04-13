# Import your environment class
from packaging_env import PackagingFragilityEnv  # or define it above if you're not importing
import gymnasium as gym
from gymnasium.wrappers import TimeLimit


# ✅ Create the environment with rendering enabled
env = PackagingFragilityEnv(render_mode="human")

# Wrap with a time limit (e.g., 50 steps)
env = TimeLimit(env, max_episode_steps=100_000)

# ✅ Reset the environment
obs, _ = env.reset()
done = False
truncated = False
step_count = 0

# ✅ Run one episode
while not (done or truncated):
    action = env.action_space.sample()  # Replace with model.predict(obs) if using a trained agent
    obs, reward, done, truncated, _ = env.step(action)
    env.render()  # Render the environment (e.g., 60 FPS GUI update)
    step_count += 1
    print(f"Step {step_count}, Reward: {reward}, Done: {done}, Truncated: {truncated}")

# ✅ Cleanup
env.close()
