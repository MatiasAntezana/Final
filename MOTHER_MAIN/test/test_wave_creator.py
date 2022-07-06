import unittest
import numpy as np


from wave_creator import create_wave_file

class Test_create_wave_file(unittest.TestCase):

    def test_array_type(self):
        """ 
        Test if the frames are an array type object
        """
        frames=np.array([1,2,3,4,5,6,7,8])
        self.assertRaises(TypeError, create_wave_file, frames)

    def test_frames__type(self):
        """
        Test if the frames are a dict type object. 
        """
        frames= {1:2,3:4,5:5,6:6,7:8}
        self.assertRaises(TypeError, create_wave_file,frames)

    def test_frames_type2(self):
        """
        Test if the frames are an int type object.
        """
        frames=123
        self.assertRaises(TypeError, create_wave_file, frames)

    def test_frames_type3(self):
        """
         Test if the frames are an string type object.
        """
        frames="python"
        self.assertRaises(TypeError, create_wave_file, frames)


    def test_sampling_rate(self):
        """
        Test sampling rate are 0 or a negative number
        """
        sr=0
        if sr<=0:
            self.assertRaises(ValueError, create_wave_file,sr)
        else:
            pass

    def test_sampling_rate_type(self):
        """ 
        Test sampling rate type are a string type object
        """
        sr="synthesizer"
        self.assertRaises(TypeError, create_wave_file, sr)

    def test_sampling_rate_type2(self):
        """
        Test sampling rate type 2 are a none type object

        """
        sr=type(None)
        self.assertRaises(TypeError, create_wave_file, sr)

        
if __name__ == '__main__':
    unittest.main()

        
    



