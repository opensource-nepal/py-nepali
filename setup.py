"""
setup file for nepali package

- Publish version
$ python setup.py publish

- Alternative
pip install build
python -m build
"""


import os
import sys
import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()


if sys.argv[-1] == 'publish':
	if os.system("pip3 freeze | grep twine"):
		print("twine not installed.\nUse `pip install twine`.\nExiting.")
		sys.exit()
	os.system("rm -rf dist")
	os.system("python3 setup.py sdist bdist_wheel")
	os.system("twine upload dist/*")
	sys.exit()


setuptools.setup(
	name="nepali",
	version="0.5.6",
	author="Ajesh Sen Thapa",
	author_email="aj3sshh@gmail.com",
	description="nepalidatetime compatible with python's datetime feature. Converting nepali date to english, parsing nepali datetime, nepali timezone, and timedelta support in nepali datetime",
	long_description=long_description,
	long_description_content_type="text/markdown",
	keywords=['nepali date conversion', 'convert date', 'nepali date time', 'python convert date', 'parse nepali date time'],
	url="https://github.com/aj3sh/nepali",
	packages=setuptools.find_packages(),
	test_suite='nepali.tests',
	install_requires=[
		'pytz'
	],
	classifiers=[

		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
	],
)
