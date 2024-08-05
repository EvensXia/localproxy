# Makefile for EasyCamera project

# Define the virtual environment path
VENV_PATH = $(shell poetry env info --path 2>/dev/null)

# Install dependencies
install:
	poetry install

# Format code using isort and autopep8
format:
	poetry run isort .
	poetry run autopep8 --max-line-length 120 --in-place --aggressive --aggressive -r . 

# Check if virtual environment is active
venv:
ifeq ($(VENV_PATH),)
	$(error Poetry virtual environment is not active. Run 'poetry shell' to activate it)
endif

# Format code with virtual environment check
format-with-venv: venv format

# Install dependencies with virtual environment check
install-with-venv: venv install
