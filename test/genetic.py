'''
This script execute the kinematics and inverse kinematics computation.
Firstly, a set of joint angles must be inputed, used in the direct kinematic 
movement. Then, with the encountered position and orientation the inverse kinematics
is applied to verify if the same joint angles are found.

With the conda environment activated this script will run using 
----> make kinematics.
'''
import numpy as np
from src.mentor import Mentor
from src.utils.input import input_angles

if __name__ == "__main__":
    robot = Mentor()
    angles  = input_angles()
    pos, rot = robot.get_position(angles)
    print('Position Vector: ')
    print(pos)
    print('Rotation Matrix: ')
    print(rot)
    print('Thetas: {}'.format(180*np.array(robot.get_angles(pos,rot)[1])/np.pi))
    print('Inverse Kinematics Computation: {}'.format(robot.get_position(robot.get_angles(pos,rot)[1])))