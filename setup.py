from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in project_library/__init__.py
from project_library import __version__ as version

setup(
	name="project_library",
	version=version,
	description="testing",
	author="Naveen",
	author_email="naveens10102002@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
