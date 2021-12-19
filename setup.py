
from setuptools import setup, find_packages

setup(
    name='equals',
    version='0.2.0',
    packages=find_packages(include=["equals", "equals.*"]),
    install_requires=[
        'docopt',
    ],
    entry_points={
        'console_scripts': [
            'equals = equals.cli:main',
        ],
    },
)
