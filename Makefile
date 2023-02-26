##
# py-nepali
#
# @file
# @version 0.1
install:
	pip install -r requirements.txt
	pre-commit install

test:
	python -m unittest discover nepali/tests -v

coverage:
	coverage run -m unittest discover nepali/tests -v
	coverage report

coverage-html:
	rm -rf htmlcov
	coverage run -m unittest discover nepali/tests -v
	coverage html
	open htmlcov/index.html
