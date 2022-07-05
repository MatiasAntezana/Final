#%%
import numpy as np
#hará que me reproduzca dos notas al mismo tiempo
import argparse #Para poder ejecutar el código en consola 
import sys #Para que pueda salir del sistema
from sintetiza_class import Sound
from read_score import organization
from wave_creator import create_wave_file
from FOLDER_MIDI.prueba import hola
print(hola())

def main ():
    """
    Function that recreates the argparse to be able to execute the program through the system console.

    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-f",type=int,default=44100,help="Elige una frecuencia de mostreo")
    parser.add_argument("-s",default="debussy_note.txt",help="Escriba una partitura")
    parser.add_argument("-a",default="audio.wav",help="Escriba un nombre para el archivo wave")
    args = parser.parse_args()
    sys.stdout.write(str(menu(args)))

def menu(args):
    """ # Falta instrumento
    Main function with which the program will run, including the synthesizer.
    Parameters:
    ----------
        frequency:int -> Sampling frequency
        instrument -> Instrumento #falta
        score:txt -> The sheet music
    """
    clas_c = Sound()
    #list_p = music_debussy(args.score)
    #list_1 = list_p[0]
    #list_2 = list_p[1]
    #list_3 = list_p[2]
    #list_4 = list_p[3]
    list_org = organization(args.s)
    list_1 = list_org[0]
    list_2 = list_org[1]
    list_3 = list_org[2]
    notes = []
    for i in list_1:
        note_music = clas_c.dic_notes[i]
        notes.append(note_music)
    frames = []
    num = 0
    for note in notes:
        #sonido = clas_c.play(note,1,44100) #Hara que suene el sonido
        onda = clas_c.create_data(note,float(list_2[num]),float(list_3[num]),args.f)
        num += 1
        frames.append(onda)
    create_wave_file(frames,args.a)
    return "Fin"

"""python menu.py --frequency=44100 --score=debussy_note.txt --audio=au.wav"""

if __name__=="__main__":
    main()