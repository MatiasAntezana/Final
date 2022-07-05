from fileinput import filename
from unicodedata import name
import unittest
from read_instrument import *


class test_read_instrument(unittest.TestCase):

    def test_read_instrument(self):
        try:
            with open("test_read_instru.txt","r") as mem:
                for line in mem:
                    line = line.strip()
                    line = int(line)
        except:
            self.assertRaises(ValueError, read_instru(filename))

if __name__ == "__main__":
    unittest.main()
