
import unittest

class test_music_debussy(unittest.TestCase):

        def test_1(self,list_1,list_2):
                list_1=[1,2,3]
                list_2=[1,2,3,4]
                self.assertEqual(list_2==list_1)
        
        

if __name__ == '__main__':
        unittest.main()


