'''
This script is responsible to define the module 
for an element of the population of the genetic algorithm. 

This package/module can be imported using:
from src.models.node import Node
'''

import numpy as np
from src.mentor import Mentor
from src.polynomial import Polynomial
from src.utils.numerical import create_angles
from src.utils.constants import MAXIMUM_VELOCITY, POINTS

class Node:
    '''
    Node is the class used to build an element of the population 
    in the genetic algorithm. This class can be defined as a Mentor Robot
    with its movements defined by values of initial and final
    angles inputed.

    Attributes
    ----------
    joint : list
        List containing time, angles and angular velocities.
    dist: int
        Distance traveled by the end effector grip.
    points: int
        Cartesian coordiantes traveled by the mentor robot.
    angle: Numpy Array
        Bi-dimensional array of angles of all joints through time.
    constraint: bool
        Tag used to identify if any physical constraint has been violated.

    Methods
    -------
    find_points(self):
        Method for calculate the position in each instant of the simulation 
        and evaluate the total distance traveled by the end effector grip.

    test_velocity(self):
        Method for testing if the robot isn't violating any physycal or
        practical constraint due the polynomes randomly generated.
    '''
    def __init__(self, thetas_i, thetas_f, time, steps):
        '''
        Node class constructor.

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
        '''
        times, thetas, omegas = [], [], []
        angles_elements = [list(create_angles(theta_i, theta_f, time, steps)) for theta_i, theta_f in zip(thetas_i, thetas_f)]
        for i in range(5):
            deltas, delta_thetas, delta_omegas = create_angles(thetas_i[i], thetas_f[i], time, steps)
            times.append(deltas)
            thetas.append(delta_thetas)
            omegas.append(delta_omegas)
        self.steps = steps
        self.time = time
        self.joint = [[times[i], thetas[i], omegas[i]] for i in range(5)]

    def find_points(self):    
        '''
        Method to create trajectory and verify distance and 
        constraints violation.
        
        Parameters
        ----------
        This method doesn't receive any parameter.
        '''
        mentor = Mentor()
        points, polynomies = [], []
        for j in range(self.steps-1):
            sub_polynomies = []
            for i in range(5):
                sub_polynomies.append(Polynomial(self.joint[i][0][j], self.joint[i][0][j+1], self.joint[i][1][j], self.joint[i][1][j+1], self.joint[i][2][j], self.joint[i][2][j+1], number=POINTS))
            polynomies.append(sub_polynomies)
        angles = [np.array([]) for i in range(5)]
        for i in range(self.steps-1):
            for j in range(len(angles)):
                if i == 0:
                    angles[j] = np.concatenate((angles[j], polynomies[i][j].thetas))
                else:
                    angles[j] = np.concatenate((angles[j], polynomies[i][j].thetas[1:]))
        index = np.min([angles[i].shape[0] for i in range(5)])
        self.angle = [angles[i][0:index] for i in range(5)]
        dist = 0 
        for i, angle in enumerate(np.transpose(self.angle)):
            new_pos, rot = mentor.get_position(angle, z_axis=5)
            if i != 0:
                dist+=np.sqrt((old_pos[0]-new_pos[0])**2+(old_pos[1]-new_pos[1])**2+(old_pos[2]-new_pos[2])**2)
            old_pos = new_pos
            points.append(new_pos[0:3])
        self.dist = dist
        self.points = points
        self.constraint = False
        self.test_velocity()

    def test_velocity(self):
        '''
        Method to examine if robot movement violate any 
        physical or practical constraint.
        
        Parameters
        ----------
        This method doesn't receive any parameter.
        '''
        for i in range(self.angle[0].shape[0]-1):
            for j in range(5):
                if abs(self.angle[j][i+1]-self.angle[j][i])/(self.time/self.angle[j].shape[0]) > MAXIMUM_VELOCITY:
                    self.constraint = True
                    break
            if self.constraint:
                break                