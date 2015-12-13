.PHONY: test run dist

test:
	@PYTHONPATH=. nosetests --with-xunit -vdw test

build:
	pip install -r requirements.txt

dist:
	@tar cvzf dist/app.tgz app run_* Makefile

run:
	@./run_dev.py
