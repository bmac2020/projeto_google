#!/usr/bin/python3
#-*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open("README.rst") as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name="algoritmo_google",
    version="0.1.0",
    description="Projeto de Modelagem Matemática - PageRank",
    long_description=readme,
    author="Gabriel Milani, Guilherme Ventura, Milton Leal, Richard Sousa",
    author_email="gabriel.milani@usp.br, guilhermeventura@usp.br, milton.leal@usp.br, richardsousa@usp.br",
    url="https://github.com/bmac2020/projeto_google",
    license=license,
    packages=find_packages(exclude="tests")
)
