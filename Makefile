install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C random.py

format:
	black *.py

test:
	python random.py