#Part 1: Integrating Your Environment with Stable-Baselines3
#✅ Step 1: Wrap your environment
from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env
#from stable_baselines3.common.vec_env import DummyVecEnv
from packaging_env import PackagingFragilityEnv  # Save the above code in packaging_env.py
#Add Callbacks (for saving best model, early stopping, etc.)
from stable_baselines3.common.callbacks import EvalCallback
from stable_baselines3.common.monitor import Monitor
import gymnasium as gym
from gymnasium.wrappers import TimeLimit

import shutil
shutil.rmtree('./ppo_logs', ignore_errors=True)
shutil.rmtree('./logs', ignore_errors=True)


eval_env = PackagingFragilityEnv(render_mode="human")
check_env(eval_env)
eval_env = Monitor(eval_env)

# Wrap with a time limit (e.g., 50 steps)
eval_env = TimeLimit(eval_env, max_episode_steps=200) 


# Monitoring Training with a Dashboard
# Enable logging
# Train the model
model = PPO("MlpPolicy", eval_env, verbose=1, tensorboard_log="./ppo_logs/", ent_coef=0.01)

# Step 2: Set up the evaluation callback
eval_callback = EvalCallback(eval_env, best_model_save_path="./logs/best_model",
                             log_path="./logs/", eval_freq=5000,
                             deterministic=True, render=False)

model.learn(total_timesteps=10_000, callback=eval_callback, tb_log_name="packaging_run")
# Save the trained model
model.save("fragility_robot_ppo")

# Load the trained model
obs, _ = eval_env.reset()
done = False
while not done:
    action, _ = model.predict(obs)
    obs, reward, terminated, truncated, _ = eval_env.step(action)
    done = terminated or truncated
    eval_env.render()  # Only if render_mode="human"
    
# Close the environment
eval_env.close()

