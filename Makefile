black:
	black **/*.py

isort:
	isort **/*.py

flake8:
	flake8 **/*.py

lint: black isort flake8
