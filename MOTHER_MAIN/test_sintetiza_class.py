

import unittest 
from sintetiza_class import Sound


class Sintetizaclass(unittest.TestCase):
    """
    Class test for Sound class from sintetiza_class.py, that
    represents the syntethizer.

    ...

    Atributtes
    ----------
        None
    
    Methods
    -------

        test_create_list_int():
            Check if lista is an int type.

        test_create_list_str():
            Check if lista is a string type.

        test_create_list_None():
            Check if lista is a None type.



    """

    def test_create_list_int(self):
        """
        Check if lista is an int type.
        """
        lista=440
        self.assertRaises(TypeError,Sound.create_data,lista)

    def test_create_list_str(self):
        """
        Check if lista is a string type.
        """
        lista="syntethizer"
        self.assertRaises(TypeError,Sound.create_data,lista)

    def test_create_list_None(self):
        """
        Check if lista is a None type.
        """
        lista=None
        self.assertRaises(TypeError,Sound.create_data,lista)


if __name__ == '__main__':
    unittest.main()
    
    
    

