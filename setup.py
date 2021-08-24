#!/usr/bin/env python

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='atimage',
    version='0.0.1',
    description='image processing utilties',
    author='Stelios Papadopoulos, Tony Ramos',
    license="GNU LGPL",
    url='https://github.com/cajal/at-image',
    author_email='spapadop@bcm.edu',
    packages=find_packages(exclude=[]),
    install_requires=['numpy', 'scipy', 'matplotlib', 'pandas', 'scikit-image']
)