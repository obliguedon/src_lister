#! /usr/bin/python

from setuptools import setup, find_packages

setup(
    name="src_lister",
    version='0.1',
    packages=find_packages(),  # python package names here
    scripts=['sources/main.py'],  # scripts here
    package_data='': ['*.yml'],

    #metadata
    author='obliguedon',
    author_email='none for now',
    description='Get all the files listed in multiples YAML files referencing each other',
    license='GPLv3',
    keywords='HDL sources listing',
    url='https://github.com/obliguedon/src_lister',
)
