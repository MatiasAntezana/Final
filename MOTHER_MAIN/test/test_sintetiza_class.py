

import unittest 
from sintetiza_class import Sound,create_data


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

        test_framerate_type():
            Check if framerate is an string type.

        test_framerate_type2():
            Check if framerate is a None type.



    """

    def test_create_list_int(self):
        """
        Check if lista is an int type.
        """
        lista=440
        self.assertRaises(TypeError,create_data,lista)

    def test_create_list_str(self):
        """
        Check if lista is a string type.
        """
        lista="syntethizer"
        self.assertRaises(TypeError,create_data,lista)

    def test_create_list_None(self):
        """
        Check if lista is a None type.
        """
        lista=None
        self.assertRaises(TypeError,create_data,lista)


    def test_framerate_type(self):
        """
        Check if framerate is an string type.
        
        """
        framerate="44100"
        self.assertRaises(TypeError,create_data,framerate)

    def test_framerate_type2(self):
        """
        Check if framerate is a None type.
        """
        framerate=None
        self.assertRaises(TypeError,create_data,framerate)






    def test_play(self):
        pass

    def test_play_chord(self):
        pass

if __name__ == '__main__':
    unittest.main()
    
    
    

