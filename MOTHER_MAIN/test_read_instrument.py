
import unittest
from read_instrument import *


class test_read_instrument(unittest.TestCase):
    """
    A class to test read_instru function from read_instrument file.
    
    ...
    
    Atributtes
    ----------
        None
    
    Methods
    --------
        test_read_instrument():
            Test to try open a txt file name error.

    """


    def test_read_instrument(self):
                """
                Test to try open a txt file name error. 
                """
                try:
                        with open("test_read_instru.txt") as file:
                                read_data=file.read()
                                return read_data
                except:
                        self.assertRaises(NameError,read_instru("test_read_instru.txt"))

if __name__ == "__main__":
    unittest.main()
