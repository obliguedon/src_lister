#! /usr/bin/python

from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description_txt = (this_directory / "README.md").read_text()

setup(
    long_description=long_description_txt,
    long_description_content_type='text/markdown'
)
