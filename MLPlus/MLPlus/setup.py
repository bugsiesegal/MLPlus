from setuptools import setup
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "MLPlus",
    version = "0.0.1",
    author = "Bugsie Segal",
    description = ("Screw dataprocessing"),
    license = "BSD",
    keywords = "example documentation tutorial",
    url = "",
    packages=['an_example_pypi_project', 'tests'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 0 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ]
)