from setuptools import setup, find_packages

# with open("requirements.txt") as f:
#     required = f.read().splitlines()

setup(
    name="weatherCLI",
    version="1.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    entry_points={"console_scripts": ["weatherCLI = weatherCLI.weatherCLI:main"]},
    install_requires=["requests",'pytz'],
)
