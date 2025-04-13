# Reinforcement Learning for Robotic Packaging Optimization

This project simulates a robotic packaging environment using PyBullet, focusing on developing and evaluating reinforcement learning (RL) strategies for robotic manipulation tasks. The simulation features a Franka Panda robotic arm performing object manipulation tasks, including picking and placing objects on a tray. The goal is to establish a foundation for RL-based control in the future.

## 🧠 Project Overview

- **Simulation Environment**: Utilizes PyBullet to create a realistic physics-based simulation of a robotic packaging scenario
- **Robotic Arm**: Incorporates the Franka Panda robotic arm for executing pick-and-place tasks
- **Reinforcement Learning Integration**: Lays the groundwork for applying RL algorithms to optimize robotic packaging strategies

## 📁 Repository Structure

- `main.py` Main script to initialize and run the simulation environment.
- `packaging_env.py` Defines the custom packaging environment compatible with OpenAI Gym standard.
- `test_env.py` Contains test cases to validate the environment's functionality.
- `test1.py` Additional testing script for environment interaction.
- `requirements.txt` Lists the Python dependencies required to run the project.
- `ppo_logs/packaging_run_1/` Directory containing logs from a Proximal Policy Optimization (PPO) training run.
- `fragility_robot_ppo.zip` Archived model or data related to PPO training.

## ⚙️ Installation & Setup

### Prerequisites

Ensure you have the following installed:

 Python 3x, 
 PyBullet, 
 Numpy

### Installation Steps

1 Clone the repository:

   ```bash
   git clone https://github.com/Messiri4/reinforcement-learning-robotic-packaging-optimization.git
   cd reinforcement-learning-robotic-packaging-optimization
   ```


2 Install the required Python package:

   ```bash
   pip install -r requirements.txt
   ```


## 🚀 Running the Simulation

To start the simulation


```bash
python3 main.py
```


This will launch the PyBullet simulation environment with the Franka Panda robotic arm ready to interact.

## 🧪 Testing the Environment

To run the test cases and validate the environment:


```bash
python3 test_env.py
```

This script will execute predefined tests to ensure the environment's components function as expected.

## 🤖 Reinforcement Learning Integration

The project is structured to facilitate the integration of the RL algorithm. The `packaging_env.py` file defines the environment in a manner compatible with RL libraries such as Stable Baselie3. Future work includes training and evaluating RL agents to optimize the robotic packaging process.

## 📄 Licnse

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📬 Contact

For questions or collaborations, please contact Miracle Messiri at messirimiracle@gmail.com.
---

This `README.md` provides a comprehensive overview of the project, guiding users through setup, execution, and future development directions.
