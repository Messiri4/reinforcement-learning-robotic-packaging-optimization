import os
import pybullet as p
import pybullet_data
import math


p.connect(p.GUI)
pandaUid = p.loadURDF(os.path.join(pybullet_data.getDataPath(), "franka_panda/panda.urdf"),useFixedBase=True)

# Set the URDF path correctly
urdfRootPath = pybullet_data.getDataPath()

while True:
    p.stepSimulation()
    tableUid = p.loadURDF(os.path.join(urdfRootPath, "table/table.urdf"),basePosition=[0.5,0,-0.65])
    trayUid = p.loadURDF(os.path.join(urdfRootPath, "tray/traybox.urdf"),basePosition=[0.65,0,0])
    p.setGravity(0,0,-10)
    objectUid = p.loadURDF(os.path.join(urdfRootPath, "random_urdfs/000/000.urdf"), basePosition=[0.7,0,0.1])
    p.resetDebugVisualizerCamera(cameraDistance=1.5, cameraYaw=0, cameraPitch=-40, cameraTargetPosition=[0.55,-0.35,0.2])
    p.setJointMotorControl2(pandaUid, 0, p.POSITION_CONTROL,0)
    p.setJointMotorControl2(pandaUid, 1, p.POSITION_CONTROL,math.pi/4.)
    p.setJointMotorControl2(pandaUid, 2, p.POSITION_CONTROL,0)
    p.setJointMotorControl2(pandaUid, 3, p.POSITION_CONTROL,-math.pi/2.)
    p.setJointMotorControl2(pandaUid, 4, p.POSITION_CONTROL,0)
    p.setJointMotorControl2(pandaUid, 5, p.POSITION_CONTROL,3*math.pi/4)
    p.setJointMotorControl2(pandaUid, 6, p.POSITION_CONTROL,-math.pi/4.)
    p.setJointMotorControl2(pandaUid, 9, p.POSITION_CONTROL, 0.04)
    p.setJointMotorControl2(pandaUid, 10, p.POSITION_CONTROL, 0.04)
    p.configureDebugVisualizer(p.COV_ENABLE_SINGLE_STEP_RENDERING)
