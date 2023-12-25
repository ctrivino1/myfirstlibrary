from setuptools import setup, find_packages

from setuptools import setup, find_packages

setup(
    name='myfirstlib',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
    ],
)
