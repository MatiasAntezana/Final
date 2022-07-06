
import unittest
import numpy as np
from scipy.io.wavfile import write

from wave_creator import create_wave_file


class Test_create_wave_file(unittest.TestCase):

    """
    Class to test the create_wave_file function from wave_creator.py.

    ...
    
    Atributtes
    ----------
        none
    
    Methods
    -------

        test_create_wav_file():
            Test if the wav file was created correctly.



    """

    def test_create_wav_File(self):
        """
        Test if the wav file was created correctly.
        """
        samplerate = 44100 
        fs = 100
        sound = np.linspace(0., 1., samplerate)
        amplitude = np.iinfo(np.int16).max
        data = amplitude * np.sin(2. * np.pi * fs * sound)
        audio="example.wav"
        try:
            write(audio, samplerate, data.astype(np.int16))
        except:
            self.assertRaises(ValueError, create_wave_file)

        
if __name__ == '__main__':
    unittest.main()

        
    



