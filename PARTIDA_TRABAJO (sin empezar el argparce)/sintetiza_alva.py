#%%
import numpy as np
#hará que me reproduzca dos notas al mismo tiempo
#import pyaudio
#import wave
from scipy.io import wavfile
from sintetiza_class import Sound

def music_debussy(filename):
    """
    Lee la partitura (por ahora solo las letras)
    Parametros:
    ----------
    filename -> Archivo de la partitura
    Return:
    list_notes -> Lista con las notas ordenadas según la partitura
    """
    with open(filename,"r") as debussy:
        list_1 = []
        for line in debussy:
            line = line.strip()
            list_2 = line.split(" ")
            list_2 = tuple(list_2)
            list_1.append(list_2)
        list_notes = []
        list_time = []
        for one,two,three in list_1:
            list_notes.append(two)
            list_time.append(three)
        return list_notes,list_time
    
def create_wave_file(sound):
    """
    Crea el archivo wave con el sonido
    Parametros:
    ----------
    sound -> Lista de vectores con los sonidos de las teclas
    """
    frames = np.concatenate(sound)
    #Concatena los vectores
    sr = 44100
    wavfile.write("audio.wav",sr,frames)
    
def menu():
    clas_c = Sound()
    #note_A0 = clas_c.dic_notes["A0"]
    #note_A4 = clas_c.dic_notes["A4"]
    #note_C2 = clas_c.dic_notes["C2"]
    #note_A4 = clas_c.dic_notes["A4"]
    #lista = [note_A0,note_A4,note_C2]
    #clas_c.play_chord(lista)
    lista = music_debussy("debussy_note.txt")
    print(lista)

menu()