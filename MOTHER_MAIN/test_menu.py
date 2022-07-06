
from argparse import Namespace
import unittest

import numpy as np
from menu import main, menu

class TestMain(unittest.TestCase):
    """
    Class to test the main function from menu.

    ...

    Attributes
    ----------
        none


    Methods
    -------
    test_main():

    """
    def test_main(self):
        args=type(Namespace) 
        self.assertRaises(TypeError, main, args)




class Test_Menu(unittest.TestCase):
    """ 
    Class to test the menu function from menu.py.

    ...

    Attributes
    ----------
        none

    Methods
    -------


        test_equal_list():
             Check if list_1 of notes and list_2 of initial time
            are equal.

        test_equal_list2():
             Check if list_2 of inital time and list_3 of duration time
            are the same list.

        list_notes_int():
             Test if list_notes is an int type.


    """
 
    
    def test_equal_list(self):
        """
        Check if list_1 of notes and list_2 of initial time
        are equal.
        """

        list_1=["A4","B5","C3"]
        list_2=[1.0,2.2,0.62]
        self.assertNotEqual(list_1, list_2,"list can't be equal")
    
    def test_equal_list2(self):
        """
        Check if list_2 of inital time and list_3 of duration time
        are the same list.
        """
        list_2=[1.0,1.65,0.9]
        list_3=[2.23,0.78,1.75]
        self.assertNotEqual(list_2,list_3,"List can't be equal")

    def list_notes_int(self):
        """
        Test if list_notes is an int type.

        """
        list_notes=440
        self.assertRaises(TypeError, menu, list_notes)

    



if __name__ == '__main__':
    unittest.main()

