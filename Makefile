init:
	pip install -r requirements.txt

test:
	python -m unittest discover -v ./src

start:
	python src/process.py

docs:
	cd docs && $(MAKE) singlehtml

.PHONY: init test start docs Makefile