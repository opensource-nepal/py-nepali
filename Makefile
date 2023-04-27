##
# py-nepali
#
# @file
# @version 0.2
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
