#from matplotlib import table
from atack_sus_decayed import Atack_sust_decay
import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
import threading
#hará que me reproduzca dos notas al mismo tiempo (falta)
#import pyaudio
#import wave
"""El sounddivice me permitira reproducir una onda sonora"""
from notes import dic_notes

class Sound:
    """
    A class to represent the synthesizer.
    Methods
    -------

    create_data(frequency,time,t0,framerate):
        Synthesizes the signal of the musical note to later transfer it to a wap file.
        
    """
    def __init__(self,list_number_harmonics,list_harmonics,list_type_func,list_values_func):
        """
        Constructor of the sound class, the synthesizer
        
        """
        self.dic_notes = dic_notes
        self.data = None
        self.list_number_harmonics = list_number_harmonics
        self.list_harmonics = list_harmonics
        self.list_type_func = list_type_func
        self.list_values_func = list_values_func
        """Le paso el diccionario"""

    def create_data (self,frequency,time,t0,framerate:int):
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
        ta = 0.02
        note_modified = Atack_sust_decay(self.list_type_func,self.list_values_func,ta,td)
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

# Por ahora usamos lo de arriba
#%%
    def play(self,frequency,time:int,framerate:int):
        """
        Función que reproducirá el sonido
        Frequency -> La frecuencia de la nota que lo voy a pasar
        time -> El tiempo de la nota (medido en segundos)
        framerate -> Frecuencia de mostreo (por ahora 44100)
        """
        t = np.linspace(0,time/3,int(time*framerate))
        """Mientras más chico sea el time, menos tiempo reproducirá las notas"""
        #t = np.linspace(0,1000/3000,int(framerate*1000/3000))

        print(t)
        """int(framerate*time/3000)"""
        wave = np.sin(2*np.pi * frequency * t)
        #plt.plot(wave[:1000], color = 'k', label = 'Frecuencia de notas hz')
        #plt.title('Simulacro de notas')
        #plt.xlabel('Hz')
        #plt.ylabel('Variacion')
        #plt.legend(loc=3)
        #plt.show()
        self.data = wave
        sd.play(wave,framerate)
        sd.wait()

    def play_chord(self,chord):
        """Le pasamos una lista que luego permitirá que le pasemos en simultaneo
        chord -> acorde"""
        threads = []
        for note in chord:
            freq = self.g_frequency(note,4)
            th = threading.Thread(target=lambda:self.play(freq,
            1,44100))
            th.start()
            threads.append(th)
    
        for thread in threads:
            thread.join()