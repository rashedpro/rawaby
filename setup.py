from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in rawapy/__init__.py
from rawapy import __version__ as version

setup(
	name="rawapy",
	version=version,
	description="this app for Rawaby rashed alhaweda factory",
	author="slnee",
	author_email="rashed.alqdi@slnee.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
