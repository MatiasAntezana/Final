"""
#Requiments:
Todo lo que necesita.
Las librerias que necesita.
pip install -r (nombre del archivo)

El setup -> Para que se pueda instalar el proyecto

La carpeta en donde está el proyecto:

Poner un archivo __init__.py

En el paquete no debe haber cosas que se pueden ejecutar
Ej: si al archivo note, le hago play, no tiene que haber código para ejecutar

CARPETE TEST:
No tiene que darle play, la tiene que llamar

import unittest
from xylophone.client import XyloClient
class TestXylo (unittest.TestCase):
    def function(self):
        xylo = XyloClient()
        self.assertEqual(2, 2)
CUIDADO: 

TEST:
Piensen en como romper la función
Pensemos en el test

"""