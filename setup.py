#!/usr/bin/env python
from os import path

from setuptools import find_packages, setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.rst")) as fd:
    long_description = fd.read()

requirements = [
    "click>=6.0",
    "pytest>=5.0",
]

setup(
    name="pytest_click",
    version="1.0.2",
    url="https://github.com/Stranger6667/pytest-click",
    license="MIT",
    author="Dmitry Dygalo",
    author_email="dadygalo@gmail.com",
    maintainer="Dmitry Dygalo",
    maintainer_email="dadygalo@gmail.com",
    description="Py.test plugin for Click",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Testing",
    ],
    include_package_data=True,
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=requirements,
    entry_points={
        "pytest11": [
            "pytest_click = pytest_click",
        ]
    },
)
