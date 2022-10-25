from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in slneeadmins/__init__.py
from slneeadmins import __version__ as version

setup(
	name="slneeadmins",
	version=version,
	description="slene admins",
	author="baha",
	author_email="baha@slnee.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
