#!/bin/env python
# -*- coding: utf8 -*-

from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

version = "0.1.0"

setup(
    name="sentimentanalysis",
    version=version,
    description="Sentiment Analysis for CSH webnews",
    classifiers=[],
    keywords="",
    author="ahanes",
    author_email="ahanes@csh.rit.edu",
    url="None",
    license="None",
    packages=find_packages(
        'nltk'
    ),
    scripts=[
        "distribute_setup.py",
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "",
    ],
    #TODO: Deal with entry_points
    #entry_points="""
    #[console_scripts]
    #pythong = pythong.util:parse_args
    #"""
)