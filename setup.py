"""
setup file for nepali package

- Publish version
$ python setup.py publish

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
	version="0.4.1",
	author="Ajesh Sen Thapa",
	author_email="aj3sshh@gmail.com",
	description="Python package for nepali processes",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/aj3sh/nepali",
	packages=setuptools.find_packages(),
	install_requires=[
		'pytz==2018.9'
	],
	classifiers=[

		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
	
	],
)