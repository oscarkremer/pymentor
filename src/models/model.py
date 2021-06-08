'''
Este script define a classe da população do algoritmo genético.

Este arquivo pode ser importado como um módulo utilizando:
from src.models import Population
'''
import itertools
import random
import numpy as np
import pandas as pd
from tqdm import tqdm
from .node.node import Node
from src.utils.numerical import create_angles
from src.utils.constants import PATH

class Population:
    '''
    Class of Population, a group of Nodes that is going to be
    optimized according to the distance traveled in a certain 
    trajectory.
    
    Attributes
    ----------
    size : int
        Size of population after the process of selection.
    initial: int
        Initial size of population before genetic optimization.
    generations: int
        Number of iterations to be runned.
    p_c: float
        Probability of cross-over.
    p_m: float
        Probability of cross-over.
    mode: srt
        String that defines how the probabilities of mutation and cross-over are
        encountered. In the case of adaptive mode, the probabilities are computed 
        using statistical values of the population in a specific generation.

    Methods
    -------
    initialization(self, theta_i, theta_f, time, steps):
        Population initialization according to the parameters of the 
        movement.
    generation(self, population,  theta_i, theta_f, time, steps):
        Method to compute and run the genetic algorithm.
    save_csv(self, population, actual_best, best_of_all):
        Method to save data from the perfomance in a .csv file located 
        inside the data/ folder.
    prob_adaptation(self, fitness):
        Method to change and compute the probabilities for cross-over and 
        mutation.
    analysis(self, population):
        Method to compute statistical parameter used in adaptive mode.
    selection(self, population, number_bests = 2):
        Selection operation method.
    cross_over(self, parents, theta_i, theta_f, time, steps):
        Cross-over operation method.
    mutation(self, member, theta_i, theta_f, time, steps):
        Mutation operation method.
    '''

    def __init__(self, initial, size, generations, p_c, p_m, mode='adaptive'):
        '''
        Constructor method.

        Parameters
        ----------
        size: int
            Population size defined before the first generation.
        initial: int
            Population size defined in the selection stage.
        generations: int
            Number of generations used in genetic optimization.
        p_c: float
            Probability for cross-over.
        p_m: float
            Probability for mutation.
        mode: str (opcional)
            Probabilities adaptation mode.
        '''
        self.size = size
        self.initial = initial
        self.generations = generations
        self.p_c = p_c
        self.p_m = p_m
        self.mode = mode

    def initialization(self, theta_i, theta_f, time, steps):
        '''
        Population initialization according to the parameters of the 
        movement.

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
        -------
        population: list
            List of Node elements and its metrics.
        '''
        population = []
        i = 0
        while i < self.initial:
            element = Node(theta_i, theta_f, time, steps)
            element.find_points()
            if not element.constraint:
                i+=1
                metric = element.dist
                population.append([metric, element])
        return population
    
    def generation(self, population,  theta_i, theta_f, time, steps):
        '''
        Method to compute and run the genetic algorithm.

        Parameters
        ----------
        population: list
            Lista de elements e métrica, que contém cada elemento
            com seu respectivo desempenho.
        theta_i: list
            List of joints initial angles.
        theta_f: list
            List of joints final angles.
        time: list
            Time duration of the movement.
        steps: list
            Number of sub-polynomes used to create a joint trajectory.
        '''
        best_of_generation = []
        actual_best = []
        for i in tqdm(range(self.generations)):
            population = self.selection(population, number_bests = self.size)
            actual_best.append(self.selection(population, number_bests = 1)[0][0])
            self.analysis(population)
            members = [member[1] for member in population]
            combinations = list(itertools.product(members, repeat=2))
            for combination in combinations:
                new_element = self.cross_over(combination)
                new_element.find_points()
                if not new_element.constraint:
                    population.insert(len(population), [new_element.dist, new_element]) 
            self.analysis(population)
            for member in population:
                mutation = self.mutation(member, theta_i, theta_f, time, steps)
                mutation.find_points()
                if not mutation.constraint:
                    population.append([mutation.dist, mutation])
            best_of_generation.append(self.selection(population, number_bests = 1)[0][0])
            best_generation = self.selection(population, number_bests = 1)[0]
        best_of_all = self.selection(population, number_bests = 1)[0]
        self.save_csv(actual_best, best_of_all)


    def save_csv(self, actual_best, best_of_all):
        '''
        Method to save data from the perfomance and points traveled in the
        cartesian space in csv's files located 
        inside the data/ folder.

        Parameters
        ----------
        actual_best: list
            List containing best performance in the population in 
            each generation.
        best_of_all: Node
            Element from the Node class that have encountered the 
            best trajectory from all.
        '''
        dataframe, points = pd.DataFrame(), pd.DataFrame()
        dataframe['distance'] = actual_best
        x, y, z = [], [], []
        for point in best_of_all[1].points:
            x.append(point[0])
            y.append(point[1])
            z.append(point[2])          
        points['x'] = x
        points['y'] = y
        points['z'] = z
        for i in range(5):
            points['theta{}'.format(i+1)] = best_of_all[1].angle[i]
        points.to_csv('data/results/points.csv', index=False)
        dataframe.to_csv('data/results/results.csv', index=False)

    def prob_adaptation(self, fitness):
        '''
        Method to change and compute the probabilities for cross-over and 
        mutation.

        Parameters
        ----------
        fitness: float
            Performance metric from a specific element of the Population.
        '''
        if self.mode == 'adaptive':
            if fitness > self.average and (self.maximum-self.average) > 0.00001:
                self.p_c = (self.maximum-fitness)/(self.maximum-self.average)
                self.p_m = (self.maximum-fitness)/(self.maximum-self.average)
            else:
                self.p_c = 0.7
                self.p_m = 0.8

    def analysis(self, population):
        '''
        Method to compute statistical parameter used in adaptive mode.

        Parameters
        ----------
        population: list
            List of Node elements and its metrics.
        '''
        fitness = [1/member[0] for member in population]
        self.std = np.std(np.array(fitness))
        self.maximum = max(fitness)
        self.average = sum(fitness)/len(fitness)

    def selection(self, population, number_bests = 2):
        '''
        Selection operation method.

        Parameters
        ----------
        population: list
            List of Node elements and its metrics.
        number_bests: integer (opcional)
            Number of best element selected.
            (default=2)

        Returns
        -------
        List of best elements in the population, ordered by the inverse of 
        traveled distance.
        '''
        return (sorted(population, key = getitem))[0:number_bests]
   
    def cross_over(self, parents):
        '''
        Cross-over operation method.

        Parameters
        ----------
        parents: list
            List containing a pair of Node elements.
        
        Returns
        -------
        New element created from the exchange of information between the parents.
        '''
        self.prob_adaptation(1/parents[0].dist)
        for i in range(5):
            if random.random() <= self.p_c:
                parents[0].joint[i] = parents[1].joint[i]
        return parents[0]

    def mutation(self, member, theta_i, theta_f, time, steps):
        '''
        Mutation operation method.

        Parameters
        ----------
        member: list
            List containin a Node element and its metric.
        theta_i: list
            List of joints initial angles.
        theta_f: list
            List of joints final angles.
        time: list
            Time duration of the movement.
        steps: list
            Number of sub-polynomes used to create a joint trajectory.

        Returns
        -------
        New element created from the mutation operation.
        '''
        element = Node(theta_i, theta_f, time, steps)
        for i in range(5):
            element.joint[i] = member[1].joint[i]
        self.prob_adaptation(1/member[0])
        for i in range(5):
            if random.random() <= self.p_m:
                deltas, delta_thetas, delta_omegas = create_angles(theta_i[i], theta_f[i], time, steps)
                member[1].joint[i] = [deltas, delta_thetas, delta_omegas]
        return member[1]

def getitem(item):
    return item[0]