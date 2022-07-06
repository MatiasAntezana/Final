#from matplotlib import table
from atack_sus_decayed import Atack_sust_decay
import numpy as np
import threading
from notes import dic_notes

class Sound:
    """
    A class to represent the synthesizer.
    Arguments:
    ----------
        list_number_harmonics:list -> List of numbers that are next to the harmonics
        list_harmonics:list -> List of harmonics
        list_func:list -> List of attack, sustain and decay types, along with their values ​​(attack, sustain and decay time)
    Methods
    -------

    create_data(frequency,time,t0,framerate):
        Synthesizes the signal of the musical note to later transfer it to a wap file.
        
    """
    def __init__(self,list_number_harmonics,list_harmonics,list_func):
        """
        Constructor of the sound class, the synthesizer
        
        """
        self.dic_notes = dic_notes
        self.data = None
        self.list_number_harmonics = list_number_harmonics
        self.list_harmonics = list_harmonics
        self.list_func = list_func

    def create_data (self,frequency,time,framerate:int):
        """
        Synthesizes the note signal by taking the frequency of the note, the duration of the note, the instant in time the note is played, and the sample rate.
        
        Arguments:
        ----------
            frequency -> Frecuencia de la nota
            time -> Tiempo de duración de la nota
            t0 -> El instante de tiempo en el que se reproduce la nota
            framerate -> La frecuencia de muestreo

        Return:
            self.data -> Devuelve la nota en forma de lista
            framerate=44100
        """
        td = 0.06
        t = np.linspace(0,time +td ,int((time+td)*framerate))
        lista_2 = [0] + self.list_harmonics
        wave_note = 0
        #print(lista_2)
        for e in range (1,len(self.list_number_harmonics)+1):
            wave_note = wave_note + e * np.sin(2*np.pi * frequency * lista_2[e] * t)
        note_modified = Atack_sust_decay(self.list_func)
        result = note_modified.main_method(t,wave_note)
        self.data = result
        """
        plt.plot(self.data[:1000], color = 'k', label = 'Frecuencia de notas hz')
        plt.title('Simulacro de notas')
        plt.xlabel('Hz')
        plt.ylabel('Variacion')
        plt.legend(loc=3)
        plt.show()
        """
        return self.data