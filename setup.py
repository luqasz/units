# -*- coding: UTF-8 -*-

import os
from setuptools import setup

here = os.path.dirname(__file__)

setup(
    zip_safe=False,
    name='units',
    version='0.1.0',
    description='Python library for handling units',
    author='Łukasz Kostka',
    author_email='lukasz.kostka@netng.pl',
    url='https://github.com/luqasz/units',
    packages=['units'],
    keywords='units si imperial',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries',
    ]
)

