#%%
import numpy as np
#hará que me reproduzca dos notas al mismo tiempo
import argparse #Para poder ejecutar el código en consola 
import sys #Para que pueda salir del sistema
#import pyaudio
#import wave
from scipy.io import wavfile
from sintetiza_class import Sound
from read_score import music_debussy

def create_wave_file(sound):
    """
    Crea el archivo wave con la señal de la nota.
    Parametros:
    ----------
        sound -> Lista de vectores con los sonidos de las teclas
    """
    frames = np.concatenate(sound)
    #Concatena los vectores
    sr = 44100
    wavfile.write("audio.wav",sr,frames)

def main ():
    parser = argparse.ArgumentParser()
    parser.add_argument("--frequency",type=int,default=44100,help="Elige una frecuencia de mostreo")
    parser.add_argument("--score",type=str,default="debussy_note.txt",help="Escriba una partitura")
    args = parser.parse_args()
    sys.stdout.write(str(menu(args)))
    

def menu(frequency,score):
    """ # Falta instrumento
    Main function with which the program will run, including the synthesizer.

    Parameters:
    ----------
        frequency -> Frecuencia de mostreo
        instrument -> Instrumento #falta
        score -> La partitura
    """
    clas_c = Sound()
    list_p = music_debussy(score)
    list_1 = list_p[0]
    list_2 = list_p[1]
    list_3 = list_p[2]
    notes = []
    for i in list_1:
        note_music = clas_c.dic_notes[i]
        notes.append(note_music)
    frames = []
    num = 0
    for note in notes:
        #print(note)
        #sonido = clas_c.play(note,1,44100) #Hara que suene el sonido
        onda = clas_c.create_data(note,float(list_2[num]),float(list_3[num]),frequency)
        num += 1
        frames.append(onda)
    #print(frames)
    create_wave_file(frames)
    #print(frames)
    print('Terminó')

if __name__=="__main__":
    menu(44100,"debussy_note.txt")