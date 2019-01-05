#!/usr/bin/env python
# coding: utf-8
import sys
import platform

from setuptools import setup
from setuptools.command.test import test as TestCommand


PYPY = hasattr(sys, 'pypy_translation_info')
PYPY3 = PYPY and sys.version_info[0] == 3


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', 'Arguments to pass into py.test')]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


requirements = [
    'click>=6.0',
    'pytest>=3.6.0',
]

test_requirements = ['pytest-cov>=1.8']

if sys.version_info < (3, 3):
    test_requirements.append('mock==1.0.1')

setup(
    name='pytest_click',
    version='0.2',
    packages=['pytest_click'],
    url='https://github.com/Stranger6667/pytest-click',
    license='MIT',
    author='Dmitry Dygalo',
    author_email='dadygalo@gmail.com',
    maintainer='Dmitry Dygalo',
    maintainer_email='dadygalo@gmail.com',
    description='Py.test plugin for Click',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Testing',
    ],
    cmdclass={'test': PyTest},
    include_package_data=True,
    install_requires=requirements,
    tests_require=test_requirements,
    entry_points={
        'pytest11': [
            'pytest_click = pytest_click',
        ]
    },
)
