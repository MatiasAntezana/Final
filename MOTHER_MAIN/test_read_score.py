
from io import TextIOWrapper
import unittest

from read_score import org_dic, organization, separate_list




class test_organization(unittest.TestCase):
        """
        Class test for organization function from read_score.py


        ...

        Atributtes
        ----------
                None

        Methods
        -------
                test_open_file():
                        Test to try open a txt file.

        """

        def test_open_file(self):
                """
                Test to try open a txt file.
                """
                try:
                        with open("test.txt") as file:
                                read_data=file.read()
                                return read_data
                except:
                        self.assertRaises(NameError,organization("test.txt"))

       

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

        def test_sort_time(self): #No funciona
                """
                Check if the notes are sorted correctly
                """

                dic={"A4":2.5,"C6":1.20,"E5":0.65,"D4":1.90}
                list_time = []
                notes = []
                list_duration = []
                try:
                        for i in range(1,len(dic)+1):
                                time_inital = dic[i][0] 
                                note = dic[i][1]
                                duration = dic[i][2]
                                list_time.append(time_inital)
                                notes.append(note)
                                list_duration.append(duration)                                 
                except:
                        self.assertRaises(ValueError,separate_list(dic))
        


if __name__ == '__main__':
        unittest.main()


