#!/usr/bin/env python
# coding: utf-8
import sys

from setuptools import find_packages, setup

requirements = [
    "click>=6.0",
    "pytest>=3.6.0",
]

test_requirements = []

if sys.version_info < (3, 3):
    test_requirements.append("mock==1.0.1")

setup(
    name="pytest_click",
    version="0.3.1",
    url="https://github.com/Stranger6667/pytest-click",
    license="MIT",
    author="Dmitry Dygalo",
    author_email="dadygalo@gmail.com",
    maintainer="Dmitry Dygalo",
    maintainer_email="dadygalo@gmail.com",
    description="Py.test plugin for Click",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Testing",
    ],
    include_package_data=True,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=requirements,
    tests_require=test_requirements,
    entry_points={
        "pytest11": [
            "pytest_click = pytest_click",
        ]
    },
)
