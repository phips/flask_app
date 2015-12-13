.PHONY: test run dist clean

build:
	@virtualenv --system-site-packages support
	@support/bin/pip install -r requirements.txt

test: build
	@PYTHONPATH=. support/bin/nosetests --with-xunit -vdw test

dist: test
	@test -d dist || mkdir dist
	@tar cvzf dist/app.tgz app run_* Makefile support

clean:
	@rm -rf dist

run:
	@./run_dev.py
