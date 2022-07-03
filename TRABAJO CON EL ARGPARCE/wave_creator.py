import numpy as np
from scipy.io import wavfile

def create_wave_file(sound,audio):
    """
    Crea el archivo wave con la señal de la nota.
    Parametros:
    ----------
        sound -> Lista de vectores con los sonidos de las teclas
        audio -> Nombre del archivo wave
        
    """
    frames = np.concatenate(sound)
    #Concatena los vectores
    sr = 44100 #Este dependerá del instrumento o no? ¿es fijo para todos?
    wavfile.write(audio,sr,frames)