from setuptools import find_packages, setup

setup(
    name='vpc-flow-log-mapper',
    version='1.0.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'vpc-flow-log-mapper=src.main:main'
        ]
    }
)