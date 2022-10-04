install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format code
	black *.py mylib/*.py
lint:
	#flake8 pylint
	pylint --disable=R,C *.py mylib/*.py
test:
	#test
	python -m pytest -vv --cov=mylib --cov=main test_*.py
build:
	#build container
	docker build -t jangles/deploy-fastapi .
run:
	#run docker
	docker run -p 127.0.0.1:8080:8080 jangles/deploy-fastapi
deploy:
	#deploy
all: install lint test deploy