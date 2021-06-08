'''
This script defines the class of Polynomails.

This class can be imported using:
from src.polynomial import Polynomial
'''
import numpy as np


class Polynomial:
    '''
    Class of polynomial curves used during the joint trajectory generation. 

    Attributes
    --------
    t_i: float
        Initial instant of the movement.
    t_f: float
        Final instant of the movement.
    theta_i: list
        List of joints initial angles.
    theta_f: list
        List of joints final angles.
    omega_i: list
        List of joints initial angular velocities.
    omega_f: list
        List of joints final angular velocities.

    Methods
    -------    
    generate_coeff(self):
        Method to compute the coefficients in the polynomials according to
        inital and final angles, and also time instants.      
    generate_points(self, number):
        Method to create points in the discrete representation of the polynomial curves.
    '''  
    def __init__(self, t_i, t_f, theta_i, theta_f, omega_i, omega_f, number=10000):
        '''
        Polynomial class constructor.

        Parameters
        ----------
        t_i: float
            Initial instant of the movement.
        t_f: float
            Final instant of the movement.
        theta_i: list
            List of joints initial angles.
        theta_f: list
            List of joints final angles.
        omega_i: list
            List of joints initial angular velocities.
        omega_f: list
            List of joints final angular velocities.
        number: int
            Amount of sampled points of the polynomial curve.
        '''
        self.steps = number
        self.t_i = t_i
        self.t_f = t_f
        self.theta_i = theta_i
        self.theta_f = theta_f
        self.omega_i = omega_i
        self.omega_f = omega_f
        self.a = np.ones(4)
        self.generate_points(number)

    def generate_coeff(self):
        '''
        Method to compute the coefficients in the polynomials according to
        inital and final angles, and also time instants.      
        '''
        times = [[1, self.t_i, np.power(self.t_i, 2), np.power(self.t_i, 3)],
            [1, self.t_f, np.power(self.t_f, 2), np.power(self.t_f, 3)],
            [0,  1,  2*self.t_i,  3*np.power(self.t_i, 2)],
            [0,  1,  2*self.t_f,   3*np.power(self.t_f,2)]]
        coef = np.matmul(np.linalg.inv(times),np.array([[self.theta_i],[self.theta_f],[self.omega_i],[self.omega_f]]))
        self.coef = coef.reshape((coef.shape[0]))
        for index in range(self.a.shape[0]):
             self.a[index] = coef[index][0]
      
    def generate_points(self, number):
        '''
        Method to create points in the discrete representation of the polynomial curves.

        Parameters
        ----------
        number : int
            Value of sampled points of the polynomial curve.
        '''
        points = np.linspace(self.t_i, self.t_f, int(number))
        self.generate_coeff()
        self.thetas = self.a[0] + self.a[1]*(np.power(points, 1)) + self.a[2]*np.power(points, 2) + self.a[3]*np.power(points,3) 
        self.delta_thetas = self.a[1] + 2*self.a[2]*np.power(points,1) + 3*self.a[3]*np.power(points, 2)