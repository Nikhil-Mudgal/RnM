from setuptools import setup, find_packagesa

with open('requiremnents.txt') as f:
    required = f.read().splitlines()

setup(
    name = "weatherCLI",
    version = "1.0",
    package_dir={'':'src'},
    packages=find_packagesa(where='src'),
    entry_points = {'console_scripts':['weatherCLI = weatherCLI.waetherCLI:main']},
    install_requires = required
)