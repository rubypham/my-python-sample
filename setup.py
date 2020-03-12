#!/usr/bin/env python

from os.path import abspath, join, dirname
from setuptools import find_packages, setup

VERSION = 1.1
CURDIR = dirname(abspath(__file__))

with open("README.md", "r") as fh:
    long_description = fh.read()

DESCRIPTION = ('Generic automation framework for acceptance testing '
               'and robotic process automation (RPA)')
KEYWORDS = ('robotframework automation testautomation rpa '
            'testing acceptancetesting atdd bdd')
LONG_DESCRIPTION = 'My pytest'

setup(
    name         = 'mypytest',
    version      = VERSION,
    author       = 'Ruby Pham',
    author_email = 'rubyphamit@gmail.com',
    url          = 'http://robotframework.org',
    download_url = 'https://pypi.python.org/pypi/robotframework',
    license      = 'Apache License 2.0',
    description  = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    keywords     = KEYWORDS,
    platforms    = 'any',
    package_dir  = {'': 'src'},
    packages     = find_packages('src')
)
