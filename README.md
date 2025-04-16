# Reinforcement Learning for Robotic Packaging Optimization




https://github.com/user-attachments/assets/c9059017-555c-4787-a245-f8393b5964e5




This project simulates a robotic packaging environment using PyBullet, focusing on developing and evaluating reinforcement learning (RL) strategies for robotic manipulation tasks. The simulation features a Franka Panda robotic arm performing object manipulation tasks, including picking and placing objects on a tray. The goal is to establish a foundation for RL-based control in the future.

## 🧠 Project Overview

- **Simulation Environment**: Utilizes PyBullet to create a realistic physics-based simulation of a robotic packaging scenario  
- **Robotic Arm**: Incorporates the Franka Panda robotic arm for executing pick-and-place tasks  
- **Reinforcement Learning Integration**: Lays the groundwork for applying RL algorithms to optimize robotic packaging strategies  

## 📁 Repository Structure

- `main.py` – The script initializes and runs the simulation environment.  
- `packaging_env.py` – Defines the custom packaging environment compatible with the OpenAI Gym standard.  
- `test_env.py` – Contains test cases to validate the environment's functionality.  
- `test1.py` – Additional testing script for environment interaction.  
- `requirements.txt` – Lists the Python dependencies required to run the project.  
- `ppo_logs/packaging_run_1/` – Directory containing logs from a Proximal Policy Optimization (PPO) training run.  
- `fragility_robot_ppo.zip` – Archived model or data related to PPO training.  

## ⚙️ Installation & Setup

### Prerequisites

Ensure you have the following installed:

- Python (version < **3.11**, ideally **3.9.x**)  
- The **latest version of pip**  
- PyBullet  
- NumPy  

### Installation Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/Messiri4/reinforcement-learning-robotic-packaging-optimization.git
   cd reinforcement-learning-robotic-packaging-optimization
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Running the Simulation

To start the simulation:

```bash
python3 ./main.py
```

This will launch the PyBullet simulation environment with the Franka Panda robotic arm ready to interact.

## 🧪 Testing the Environment

To run the test cases and validate the environment:

```bash
python3 ./test_env.py
```

This script will execute predefined tests to ensure the environment's components function as expected.

## 📊 Visualizing Training with TensorBoard

You can monitor and visualize the training progress using **TensorBoard**.

### Steps:

1. Ensure `tensorboard` is installed (you can add it to `requirements.txt` or install it manually):

   ```bash
   pip install tensorboard
   ```

2. Start TensorBoard by pointing it to the PPO logs directory:

   ```bash
   tensorboard --logdir=ppo_logs/
   ```

3. Open your browser and navigate to:

   ```
   http://localhost:6006/
   ```

4. You will see training metrics, such as episode reward, loss, policy entropy, and more, updated in real-time.

## 🤖 Reinforcement Learning Integration

The project is structured to facilitate the integration of the RL algorithm. The `packaging_env.py` file defines the environment in a manner compatible with RL libraries such as **Stable Baselines3**. Future work includes training and evaluating RL agents to optimize the robotic packaging process.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📬 Contact

For questions or collaborations, please contact Miracle Messiri at messirimiracle@gmail.com.

---

Let me know if you’d like a sample screenshot of the TensorBoard interface or a video walkthrough to include!
