import numpy as np
from scipy.io import wavfile

def create_wave_file(sound,audio):
    """
    Function that creates the WAV file with the signal of the notes.

    --------
    Parameters:
            sound (array): array with the sounds 
            audio (str): name of the file

    Returns:
            Wave filename
        
    """
    frames = np.concatenate(sound)
    #Concatena los vectores
    sr = 44100 #Este dependerá del instrumento o no? ¿es fijo para todos?
    wavfile.write(audio,sr,frames)