
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

if __name__ == '__main__':
        unittest.main()


