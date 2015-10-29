#!/usr/bin/env python

from setuptools import setup

setup(
    name='DeCAF',
    version='1.0.1',
    description='Discrimination, Comparison, Alignment tool for small molecules',
    author='Marta M. Stepniewska',
    author_email='martasd@ibb.waw.pl',
    url='https://bitbucket.org/marta-sd/decaf',
    packages=['decaf',
              'decaf.toolkits'],
    install_requires=['numpy>=1.6.2', 'scipy>=0.10', 'matplotlib>=1.3.1']
)