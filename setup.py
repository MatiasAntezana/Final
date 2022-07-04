
from setuptools import setup, find_packages

setup(
    nombre = "tp_final" ,
    version = "1.0.0" ,
    packages= find_packages(
        where=".",
        include=[ "ejemplo proyecto" ,"ejemplo proyecto.*"])# preguntar que va aca
    install_requires = [
            "numpy>=1.23.0" ,
            "matplotlib>=3.5.2" ,
            "sounddevice>=0.4.4" ,
            "scipy>=1.8.1",
    ] 
)

setup(
    # ..., 
    setup_requires=["flake8"]  # Esto verifica el formato del codigo
)

 
setup(
    # ...,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'], #Esto instala pytest cuando se ejecutan los tests 
)