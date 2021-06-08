'''
This script defines functions for inputs of cartesian or 
joint space variables.

This module can be imported using:
from src.utils.input import input_angles, input_cartesian
'''
import numpy as np

def input_angles():
    '''
    Functions to enter with joint angles to further compute the 
    direct kinematics. The angles are entered in degrees and then converted to 
    radian.
    
    Returns
    -------
    angles
        List of joint angles.
    '''
    angles = np.zeros(5)
    for i in range(5):
        angles[i] = input('-- Theta {}: '.format(i+1))
        angles[i] = np.pi*angles[i]/180
    return angles

def input_cartesian():
    '''
    Function to input cartesian variables of position and orientation.
    The orientation angles alpha, beta and gamma (XYZ angles) are inputed 
    in degrees but then converted to radian.

    Returns
    -------
    pos: numpy array
        Array containing the three coordinates of a point in the cartesian 
        space.
    angles: numpy array
        Array containing the angles alpha, beta and gamma (XYZ angles) to represent 
        the orientation of the end effector grip of the robot.
    '''
    pos = np.zeros(3)
    angles = np.zeros(3)
    pos[0] = input('-- x (cm): ')
    pos[1] = input('-- y (cm): ')
    pos[2] = input('-- z (cm): ')
    angles[0] = np.pi*(float(input('-- alpha: ')))/180
    angles[1] = np.pi*(float(input('-- beta: ')))/180
    angles[2] = np.pi*(float(input('-- gamma: ')))/180
    return pos, angles