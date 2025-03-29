### **README: Robotic Packaging Simulation using PyBullet**

#### **Project Overview**

This project simulates a **robotic packaging environment** using **PyBullet**, a physics simulation engine. The simulation involves a **Franka Panda robotic arm** performing object manipulation tasks, including picking and placing objects on a tray. The goal is to establish a foundation for reinforcement learning (RL)-based control in the future.

---

### **Installation & Setup**

#### **1. Prerequisites**

Ensure you have the following installed:

- Python 3.x
- PyBullet (`pip install pybullet`)
- NumPy (optional for RL integration)

#### **2. Running the Simulation**

To start the simulation, run:

```bash
python test1.py
```

This initializes the PyBullet environment with the robotic arm, table, tray, and a randomly placed object.

---

### **Project Structure**

- `test1.py` → Main script that initializes the PyBullet environment and controls the robotic arm.
- `README.md` → Documentation for the project.
- `assets/` → (If applicable) Stores additional URDF models or textures.

---

### **Key Features & Components**

#### **1. Environment Setup**

- Loads a **Franka Panda robot** (URDF file).
- Adds a **table and tray** for object placement.
- Introduces a **random object** for interaction.
- Sets **gravity (-9.81 m/s²)** for realistic physics.

#### **2. Robot Control**

- Uses **position control** to set predefined joint angles.
- Controls **gripper joints** to simulate grasping.
- Executes continuous simulation with `p.stepSimulation()`.

#### **3. Camera & Visualization**

- Customizes **camera angle and zoom** for better visibility.
- Enables **single-step rendering** for debugging.

---

### **Future Improvements**

✅ Integrate **Reinforcement Learning (RL)** for adaptive control.  
✅ Implement a **reward function** for evaluating success/failure.  
✅ Enhance **object physics** with better friction and collision parameters.  
✅ Optimize **action space** for more efficient object handling.

---

### **License**

This project is for research and educational purposes. Free to use and modify.
