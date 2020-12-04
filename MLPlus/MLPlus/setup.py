from setuptools import *
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "MLPlus",
    version = "0.0.1",
    author = "Bugsie Segal",
    description = ("Screw dataprocessing"),
    license = "BSD",
    keywords = "Machine Learning",
    url = "",
    packages=find_packages(),
    long_description=read('README'),
    classifiers=[
        "Development Status :: 0 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ]
)