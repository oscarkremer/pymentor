# Genetic Algorithms for Trajectory Optimization

Here we submitted all code snippets to help with artificial intelligence coding to deal with an 
optimization problem, where the trajectory planning of a didactic robot is tackled.


## Install

```bash
$ make
$ make install
```

See: `Makefile` to know other commands.

## Artificial Intelligence Project

==============================

Pipeline to generate trajectories for Mentor didactic robot using artificial intelligence optimization algorithms

## Project Organization

==============================


    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make kinematics` or `make genetic`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   └── results        <- The folder to save .csv files with the performance of the model.
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    ├── environment.yml    <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > environment.yml`
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    └── src                <- Source code for use in this project.
        │
        ├── __init__.py    <- Makes src a Python module
        │
        ├── api           <- Scripts for main code
        │   │
        │   ├── kinematics.py      <- Run kinematics and inverse kinematics
        │   │
        │   └── genetic.py           <- Run genetic algorithm
        │
        ├── mentor         <- Define mentor class
        │   │   
        │   ├── __init__.py
        │   │
        │   └── mentor.py
        │
        ├── models         <- Define populaion class, and population element class
        │   │   
        │   ├── __init__.py    
        │   │
        │   ├── model.py
        │   │
        │   └── node
        │       │   
        │       ├── __init__.py
        │       │
        │       └── node.py  
        │
        ├── polinomy         <- Define Polynomial class
        │   │   
        │   ├── __init__.py
        │   │
        │   └── model.py
        │
        └── utils  <- Scripts to insert data, constants and numerical manipulations
            │   
            ├── __init__.py
            │
            ├── constants.py
            │
            ├── input.py
            │
            └── numerical.py

-------
