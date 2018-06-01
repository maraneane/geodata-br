#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (c) 2013-2018 Paulo Freitas
# MIT License (see LICENSE file)
'''
Setup script
'''
# Imports

# Built-in dependencies

import sys

from setuptools import setup, find_packages

# Compatibility check

if sys.version_info[:2] < (3, 4):
    raise RuntimeError('Python version >= 3.4 required')

# Routines

setup(
    # Package metadata
    name='geodatabr',
    version='1.0.0-dev',
    description='Brazilian territorial distribution data exporter',
    license='MIT',
    url='https://github.com/paulofreitas/geodata-br',
    author='Paulo Freitas',
    author_email='me@paulofreitas.me',

    # Package distribution
    packages=find_packages('lib'),
    package_dir={'': 'lib'},
    entry_points={
        'console_scripts': [
            'geodatabr = geodatabr.__main__:main'
        ],
    },

    # Package dependencies
    python_requires='>=3.4',
    install_requires=[
        # geodatabr.exporters package
        'fdb',
        'lxml',
        'msgpack',
        'pyyaml',
        'sqlalchemy',
        # geodatabr.parsers package
        'xlrd',
        'xlwt',
    ]
)
