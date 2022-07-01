import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
import threading
#hará que me reproduzca dos notas al mismo tiempo (falta)
#import pyaudio
#import wave
"""El soundevice me permitira reproducir una onda sonora"""
from notes import dic_notes
class Sound:
    def __init__(self):
        self.dic_notes = dic_notes
        self.data = None
        """Le paso el diccionario"""
    
    """Si lo uso para el play, está de más"""
    def g_frequency(self,note,octave):
        expo = (octave - 4) * 12 + (note - 10)
        """Note = Nota"""
        """Me dirá que tan fuerte se tiene que escuchar el sonido"""
        return 440 * ((2**(1/12))** expo)

    def create_data (self,frequency,time,framerate:int):
        """framerate=44100"""
        t = np.linspace(0,time/1,int(time*framerate))
        wave = np.sin(2*np.pi * frequency * t)
        self.data = wave
        return self.data
    
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
       # plt.title('Simulacro de notas')
       # plt.xlabel('Hz')
       # plt.ylabel('Variacion')
       # plt.legend(loc=3)
       # plt.show()
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