from setuptools import setup, find_namespace_packages

with open('requiremnents.txt') as f:
    required = f.read().splitlines()

setup(
    name = "weatherAPI",
    version = "0.0.1",
    package_dir={'':'src'},
    packages=find_namespace_packages(where='src'),
    install_requires = required
)