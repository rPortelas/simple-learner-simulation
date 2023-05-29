from setuptools import setup
import sys

assert sys.version_info.major == 3 and sys.version_info.minor >= 6, \
    "This repo is designed to work with Python 3.6 and greater." \
    + "Please install it before proceeding."

setup(
    name='teachDRL',
    py_modules=['teachDRL'],
    version="0.1",
    install_requires=[
        'scikit-learn',
        'numpy',
        'scipy',
        'treelib',
        'matplotlib',
        'seaborn',
        'imageio',
        'gym',
        'gmr',
    ],
    description="A simple environment to study teacher algorithms on simulated students",
    author="Rémy Portelas",
)
#numpy scipy treelib matplotlib
#scikit-learn seaborn imageio gym gmr