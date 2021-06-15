'''
This script allows the movement optimization executed by
Robot Mentor as published in:
A Genetic Approach for Trajectory Optimization Applied to a 
Didactic Robot. O. S. Kremer; M. A. B. Cunha; F. S. Moraes; 
S. S. Schiavon. 2019 Latin American Robotics Symposium (LARS), 
2019 Brazilian Symposium on Robotics (SBR).

To execute the optimization the user needs to insert the
initial and final position of the Mentor Robot, as well the 
initial and final orientation. The orientation is defined here 
in terms of angles alpha, beta and gamma.

With the conda environment activate this script will run using 
----> make genetic.
'''
import argparse
import numpy as np
from src.models import Population
from src.mentor import Mentor
from src.utils.input import input_cartesian


def calculate_thetas(pos, angles):
    '''
    Function to compute joint angles from position 
    and orientation.

    Parameters
    ----------
    pos : list
        List with position (x, y, z) in the cartesian space.
    angles: list
        List with the orientation XYZ of the end effector grip.

    Returns
    -------
    error
        Boolean that indicates error in movement if the pair 
        position/orientation is not physically possible.
    theta
        List containing joint angles of the robot.
    '''
    robot = Mentor()
    rot  = robot.get_orientation(angles[0], angles[1], angles[2])
    matrix_G0 = [[rot[0][0], rot[0][1], rot[0][2], pos[0]],
        [rot[1][0], rot[1][1], rot[1][2], pos[1]],
        [rot[2][0], rot[2][1], rot[2][2], pos[2]],
        [0, 0, 0, 1]]
    matrix_5G = [[1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, -5],
        [0, 0, 0, 1]]
    matrix = np.matmul(matrix_G0, matrix_5G)
    positions = [matrix[0][3], matrix[1][3], matrix[2][3]]
    error, theta = robot.get_angles(positions, rot)
    return error, theta


def enter_position():
    '''
    Function to input angles and positions until
    there exists a set of angles for such set and then 
    compute the inverse kinematics.
    
    Parameters
    ----------
    This functions doesn't have any input parameter.
    
    Returns
    -------
    theta
        List containing joint angles of the robot.
    pos
        List containing position inputed initially.
    '''
    error = True
    while error:
        pos, angles = input_cartesian()    
        error, theta = calculate_thetas(pos, angles)
        if error:
            print('Error !!! \n Position and/or orientation not possible !!! \n Please test other values!')
    return theta, pos


def main(steps, time, generations, mode, population, cross_over, mutation):
    '''
    Main function which includes insertion of desired position and orientation,
    as well instatiation of Population for genetic algorithm.

    Parameters
    ----------
    steps: int
        Number of sub-polynomials used to create a joint trajectory.
    time: float
        Time duration of the movement.
    generations: int
        Number of generations used in genetic optimization.
    mode: str
        Probabilities adaptation mode.
    population: int
        Population size defined in the selection stage.
    cross_over: float
        Probability for cross-over.
    mutation: float
        Probability for mutation.
    '''
    theta_i, pos_i = enter_position()
    theta_f, pos_f = enter_position()
    optimized = Population(population, population, generations, cross_over, mutation, mode=mode)
    population = optimized.initialization(theta_i, theta_f, time, steps)
    optimized.generation(population, theta_i, theta_f, time, steps)


if __name__ == "__main__":
    parser = argparse.ArgumentParser('Inicialization --- Optimization Algorithm')
    parser.add_argument('--mode', default='normal', type=str, 
        choices=['normal', 'adaptive'])
    parser.add_argument('--steps', default=3, type=int)
    parser.add_argument('--time', default=10, type=float)
    parser.add_argument('--generations', default=15, type=int)
    parser.add_argument('--population', default=15, type=int)
    parser.add_argument('--cross-over', default=0.9, type=float)
    parser.add_argument('--mutation', default=0.5, type=float)
    args = parser.parse_args()
    main(args.steps, args.time, args.generations, args.mode, args.population, args.cross_over, args.mutation)
