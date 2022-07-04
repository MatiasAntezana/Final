
from io import TextIOWrapper
import unittest

from read_score import music_debussy, organization, separate_list

class test_music_debussy(unittest.TestCase):
        """ 
        Class test for music_debussy function from read_score.py.

        ...

        Atributtes
        -----------
                None

        Methods
        -------
                test_check_file_type():
                        Check that the
                        file type is correct.

                test_file_type_correct():


                test_list_1_int():
                        Check if list_1 is an int type.

                test_list_1_str():
                        Check if list_1 is a string type.

                test_split():
                          Check that s.split fails
                        when the separator is not a


        """

        def check_file_type(self):
                """Check that the
                 file type is correct"""
                debussy="type"
                self.assertRaises(TypeError, music_debussy, debussy)

        def test_file_type_correct(self):
                #No estoy seguro si funciona
                debussy=TextIOWrapper
                if debussy==type(TextIOWrapper):
                        return True

                self.assertTrue(debussy)
        


        def list_1_int(self):
                """
                Check if list_1 is an int type.
                """
                list_1=1024
                self.assertRaises(TypeError, music_debussy, list_1)
        
        def list_1_str(self):
                """
                Check if list_1 is a string type.
                """
                list_1="1024"
                self.assertRaises(TypeError, music_debussy, list_1)
        

        def test_split(self):#funciona?
                """
                Check that s.split fails
                when the separator is not a
                """
                s="python"
                self.assertEqual(s.split(), ["synthesizer", "python"])
                with self.assertRaises(TypeError):
                        s.split(" ")




class test_organization(unittest.TestCase):
        """
        Class test for organization function from read_score.py


        ...

        Atributtes
        ----------
                None

        Methods
        -------
                list_1_int():
                        Check if list_1 is an int type.

                list_1_str():
                        Check if list_1 is a string type.

                dic_int():
                        Check if dic is an int type.

                dic_str():
                        Check if dic is a string type.

                dic_list():
                        Check if dic is a list type.

        """
        def list_1_int(self):
                """
                Check if list_1 is an int type.
                """
                list_1=1024
                self.assertRaises(TypeError, organization, list_1)
        
        def list_1_str(self):
                """
                Check if list_1 is a string type.
                """
                list_1="1024"
                self.assertRaises(TypeError, organization, list_1)

        def dic_int(self):
                """
                Check if dic is an int type.
                """
                dic=1024
                self.assertRaises(TypeError, organization, dic)
        
        def dic_str(self):
                """
                Check if dic is a string type.
                """
                dic="1024"
                self.assertRaises(TypeError, organization, dic)

        def dic_list(self):
                """
                Check if dic is a list type.
                """
                dic=[1024,2048,3096]
                self.assertRaises(TypeError, organization, dic)
        


class test_separate_list(unittest.TestCase):

        """
        Class test to separate_list function from read_score.py

        ...

        Atributtes
        ----------
                None

        Methods
        -------
                test_sort_time():
                        Check if the notes are sorted correctly.

        """

        def test_sort_time(self):
                """
                Check if the notes are sorted correctly
                """


                list_t0_time=[2.5,1.20,0.65,1.90,3.75]
                separate_list(list_t0_time)
                list_time=[0.65,1.20,1.90,2.5,3.75]
                self.assertEqual(list_t0_time, list_time)



if __name__ == '__main__':
        unittest.main()


