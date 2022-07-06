
from setuptools import setup, find_packages


setup(
    name = "MOTHER_MAIN" ,
    version = "1.0.0" ,
    packages=find_packages(
        where=".",
        include=[],
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