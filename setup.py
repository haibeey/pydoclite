from setuptools import find_packages, setup
import os 
from platform import system

if system()=="Linux":
    libpath="linux/docliteshared.so"
elif system()=="Darwin":
    libpath = "darwin/docliteshared.so"
else:
    raise ValueError("os platform not supported yet")

basedir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(basedir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name="pydoclite",
    packages=find_packages(),
    version="0.1.5",
    include_package_data=True,
    description="pydoclite is the python library interface for doclite",
    author="abrahamakerele38@gmail.com",
    license="MIT",
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    package_data={"": ["*"]},
    test_suite="tests",
    long_description=long_description,
    long_description_content_type='text/markdown'
)