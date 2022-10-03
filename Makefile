install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format code
lint:
	#flake8 pylint
test:
	#test
deploy:
	#deploy
all: install lint test deploy