#!/usr/bin/env python

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'requirements.txt')) as f:
    requirements = f.read().split()

setup(
    name='at-image',
    version='0.0.1',
    description='image processing utilities',
    author='Erick Cobos, Stelios Papadopoulos',
    license="GNU LGPL",
    url='https://github.com/cajal/at-image',
    author_email='spapadop@bcm.edu',
    packages=find_packages(exclude=[]),
    install_requires=requirements
)