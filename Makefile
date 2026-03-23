##
# py-nepali
#
# @file
# @version 0.2
test:
	python -m unittest discover tests -v

coverage:
	coverage run -m unittest discover tests -v
	coverage report

coverage-html:
	rm -rf htmlcov
	coverage run -m unittest discover tests -v
	coverage html
	open htmlcov/index.html
