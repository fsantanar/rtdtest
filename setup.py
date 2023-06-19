from setuptools import find_packages, setup

setup(
    name='rtdtest',
    version='1.0.0',
    packages=find_packages('src'),
    package_dir={'':'src'},
    install_requires=[
        'numpy==1.24.3',
        'PyYAML==6.0',
    ],
)
