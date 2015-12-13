.PHONY: test run dist clean

test:
	@PYTHONPATH=. nosetests --with-xunit -vdw test

build:
	pip install -r requirements.txt

dist: test
	@test -d dist || mkdir dist
	@tar cvzf dist/app.tgz app run_* Makefile

clean:
	@rm -rf dist

run:
	@./run_dev.py
