
from setuptools import setup, find_packages

setup(
    nombre = "Final" ,
    version = "1.0.0" ,
    packages=find_packages(
        where=".",
        include=[ "Final*"],
    )
)

setup(
    # ..., 
    setup_requires=["flake8"] 
)

 
setup(
    # ...,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)