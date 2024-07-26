from setuptools import setup, find_packages


def requirements_from_file(file_name):
    return open(file_name).read().splitlines()

setup(
    name='bitcoin_tools',
    version='0.1.0.n0ri',
    packages=find_packages(),
    install_requires=requirements_from_file('requirements.txt'),
)