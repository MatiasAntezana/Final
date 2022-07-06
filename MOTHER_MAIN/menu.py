#%%
import argparse
import sys
from sintetiza_class import Sound
from read_score import organization
from wave_creator import create_wave_file
from read_instrument import read_instru

def main ():
    """
    Function that recreates the argparse to be able to execute the program through the system console.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-f",type=int,default=48000,help="Choose a sample rate")
    parser.add_argument("-i",default="piano.txt",help="Choose an instrument")
    parser.add_argument("-s",default="debussy_note.txt",help="Write a sheet music")
    parser.add_argument("-a",default="audio_new.wav",help="Type a name for the wave file")
    args = parser.parse_args()
    sys.stdout.write(str(menu(args)))

def menu(args):
    """
    Main function with which the program will run, including the synthesizer.
    Parameters:
    ----------
        args.f:int -> Sampling frequency
        args.i:txt -> Instrument file name
        args.s:txt -> Score file name
        args.a:wav -> Name of the wave file to be generated

    """
    result = read_instru(args.i)
    list_number_harmonics = result[0]
    list_harmonics = result[1]
    list_func = result[2]
    clas_c = Sound(list_number_harmonics,list_harmonics,list_func)
    list_org = organization(args.s)
    list_1 = list_org[0]
    #list_2 = list_org[1]
    list_3 = list_org[2]
    notes = []
    for i in list_1:
        note_music = clas_c.dic_notes[i]
        notes.append(note_music)
    frames = []
    num = 0
    for note in notes:
        onda = clas_c.create_data(note,float(list_3[num]),args.f)
        num += 1
        frames.append(onda)
    create_wave_file(frames,args.a)
    return "Finish"
if __name__=="__main__":
    main()