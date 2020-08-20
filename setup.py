from setuptools import find_packages, setup
import os 

setup(
    name="pydoclite",
    packages=find_packages(),
    version="0.1.0",
    description="pydoclite is the python library interface for doclite",
    author="abrahamakerele38@gmail.com",
    license="MIT",
    install_requires=[],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    package_data={"pydoclite": ["docliteshared.so"]},
    include_package_data=True,
    test_suite="tests",
)