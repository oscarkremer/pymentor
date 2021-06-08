'''
This script defines the function to create the points in 
angular position, angular velocity and time to create all the 
sub-polynomial curves used in the joint trajectory curves.

This module can be imported using:
from src.utils.numerical import create_angles
'''

import random
import numpy as np

def create_angles(theta_i, theta_f, final_time, steps):
    '''
    Function to create the sub-points in the random polynomial 
    that the robots must follows in their joints.

    Parameters
    ----------

    theta_i: list
        List of joints initial angles.
    theta_f: list
        List of joints final angles.
    time: float
        Duration of the movement (measured in seconds).
    steps: int
        Number of polynomial curves that will be generated
        to create the complete joint trajectory 

    Returns
    ----------
    time: list
        List of time points to create all the sub-polynomials.
    theta: list
        List of angular position points to create all 
        the sub-polynomials.
    omega: list
        List of angular velocities points to create all 
        the sub-polynomials.
    '''
    theta, omega, time = [theta_i], [0], [0]
    for i in range(steps-2):
        theta.append((theta_f - theta_i)*random.random() + theta_i)
        omega.append(5*random.random())
        time.append(final_time*random.random())
    omega.append(0)
    theta.append(theta_f)
    time.append(final_time)
    time.sort()
    if theta_i < theta_f:
        theta.sort()
    else:
        theta.sort(reverse=True)
    return time, theta, omega        