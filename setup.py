
from setuptools import setup

setup(
    name='equals',
    version='0.1.0',
    py_modules=['equals'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'equals = equals.cli:cli',
        ],
    },
)
