from setuptools import find_packages, setup

setup(
    name='cpu_rtd_test',
    version='1.0.0',
    packages=['rtdtest'],
    install_requires=[
        'numpy==1.24.3',
        'PyYAML==6.0',
    ],
)

