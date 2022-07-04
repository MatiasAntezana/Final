
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
        args=type(Namespace) #funciona?
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
        test_class():
            test if class_c is a function.

        test_class2():
            test if class_C is an int type.

        test_class3():
            test if class_C is a string type.

        test_class4():
            test if class_C is a list type.

        test_class5():
            test if class_C is an array type.

        test_list_1_int():
            test if list_1 of notes is an int type.

        test_list_1_str():
            test if list_1 of notes is an string type.

        test_list_2_str():
            test if list_2 of initial time is
            an string type.

        test_list_2_int():
            test if list_2 of initial time is
            an int type.

        test_list_3_int():
            Test if list_3 of duration time is an int type.

        test_list_3_str():
             Test if list_3 of duration time is an str type.

        test_equal_list():
             Check if list_1 of notes and list_2 of initial time
            are equal.

        test_equal_list2():
             Check if list_2 of inital time and list_3 of duration time
            are the same list.

        list_notes_int():
             Test if list_notes is an int type.

        list_notes_str():
             Test if list_notes is an string type.


    """
 

    def test_class(self):# no se si existe
        """
        test if class_c is a function .
        """
        class_c= type (function)
        self.assertRaises(TypeError, menu, class_c)
        
    def test_class2(self):
        """ 
        test if class_C is an int type.
        """
        class_c= 23
        self.assertRaises(TypeError, menu, class_c)

    def test_class3(self):
        """ 
        test if class_C is a string type.
        """
        class_c= "23"
        self.assertRaises(TypeError, menu, class_c)

    def test_class4(self):
        """
        test if class_C is a list type
        """
        class_c= [23,24,25]
        self.assertRaises(TypeError, menu, class_c)

    def test_class5(self):
        """
        test if class_C is an array type.

        """
        class_c= np.array([1,2,3,4,5])
        self.assertRaises(TypeError, menu, class_c)




    def test_list_1_int(self): #notes
        """ 
        test if list_1 of notes is an int type.
        
        """
        list_1=1
        self.assertRaises(TypeError, menu, list_1)

    def test_list_1_str(self): #notes
        """
        test if list_1 of notes is an string type.
        
        """
        list_1="python"
        self.assertRaises(TypeError, menu, list_1)


    def test_list_2_str(self): #initial times
        """ 
        test if list_2 of initial time is
         an string type.
         """
        list_2="python"
        self.assertRaises(TypeError, menu, list_2)

    def test_list_2_int(self): #initial times
        """ 
        test if list_2 of initial time is
         an int type.
         """
        list_2=123
        self.assertRaises(TypeError, menu, list_2)


    def test_list_3_int(self):# duration times
        """
        Test if list_3 of duration time is an int type.

        """
        list_3=123
        self.assertRaises(TypeError, menu, list_3)

    def test_list_3_str(self):
        """
        Test if list_3 of duration time is an str type.
        
        """
        list_3="python"
        self.assertRaises(TypeError, menu, list_3)

    def test_equal_list(self):
        """
        Check if list_1 of notes and list_2 of initial time
        are equal.
        """

        list_1=["A4","B5","C3"]
        list_2=[1.0,2.2,0.62]
        self.assertNotAlmostEqual(list_1, list_2,"list can't be equal")
    
    def test_equal_list2(self):
        """
        Check if list_2 of inital time and list_3 of duration time
        are the same list.
        """
        list_2=[1.0,1.65,0.9]
        list_3=[2.23,0.78,1.75]
        self.assertNotAlmostEqual(list_2,list_3,"List can't be equal")

    def list_notes_int(self):
        """
        Test if list_notes is an int type.

        """
        list_notes=440
        self.assertRaises(TypeError, menu, list_notes)

    
    def list_notes_str(self):
        """
        Test if list_notes is an string type.

        """
        list_notes="synthesizer"
        self.assertRaises(TypeError, menu, list_notes)


if __name__ == '__main__':
    unittest.main()

