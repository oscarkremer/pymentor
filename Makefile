.DEFAULT_GOAL := check
PYTHON_INTERPRETER = python3
PROJECT_NAME := mentor
BLUE = \033[0;34m
DEFAULT = \033[0m
RED = \033[0;31m
WHITE = \033[1;37m
GENERATIONS = 15
POPULATION = 4
################################################################################
# COMMANDS                                                                     #
################################################################################

setup: check_environment
	@echo "---> Running setup.."
	@conda env create -q -f environment.yml --name $(PROJECT_NAME) > /dev/null
	@cp -n .env.example .env
	@echo "---> To complete setup please run \n---> source activate $(PROJECT_NAME)"

install: dirs
	@echo "---> Installing dependencies"
	@conda env update -f environment.yml

dirs:
	@echo "---> Creating data folder for results"
	@mkdir -p data/results
	@echo "---> Done"

kinematics:
	@echo "---> Running Kinematics-Algorithms"
	@$(PYTHON_INTERPRETER) src/api/kinematics.py 

genetic:
	@echo "---> Running Genetic Algorithms to Optimize Trajectory Planning"
	@$(PYTHON_INTERPRETER) src/api/genetic.py --population $(POPULATION) --generations $(GENERATIONS)

help:
	@echo "--- List of Commands ---"
	@echo "--- ${WHITE}install${DEFAULT}: Start installation of environment"
	@echo "--- ${WHITE}setup${DEFAULT}: Check environment and setup variables"
	@echo "--- ${WHITE}dirs${DEFAULT}: Create directory to save .csv files"
	@echo "--- ${WHITE}help${DEFAULT}: See list of possible commands"
	@echo "--- ${WHITE}kinematics${DEFAULT}: Run kinematics calculations for Mentor Robot"
	@echo "--- ${WHITE}genetic${DEFAULT}: Start running genetic algorithm for trajectory optimization"
	@echo "--- ${WHITE}clean${DEFAULT}: Remove unecessary files"

clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
