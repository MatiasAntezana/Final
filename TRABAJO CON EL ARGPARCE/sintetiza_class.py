#from matplotlib import table
from atack_sus_decayed import recor,m_t
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

    ---

    Attributes
    ----------
    Ninguno

    Methods
    -------

    create_data(frequency,time,t0,framerate):
        Synthesizes the signal of the musical note to later transfer it to a wap file.
        
    """
    def __init__(self):
        """
        Constructor of the sound class, the synthesizer
        
        """
        self.dic_notes = dic_notes
        self.data = None
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
        t = np.linspace(0,time,int(time*framerate))
        wave = np.sin(2*np.pi * frequency * t)
        #resultado = combo(wave,t,time,t0)
        lista = []
        conta = 0
        ta = 0.02
        td = 0.06
        con_mt_no = 0
        con_mt_si = 0
        #print(len(t))
        for t_v in t:
            wav = recor(wave,conta)
            mt = m_t(t_v,ta,td)
            if mt == 0:
                con_mt_si +=1
            elif mt != 0:
                con_mt_no +=1
            A = 5 #instrumento
            at = A * wav * mt
            lista.append(at)
            conta += 1
        #print("Lo que no son ceros son: ",con_mt_no,"y los que si son: ",con_mt_si)
        self.data = lista
        #print(self.data)
        """
        Tengo que crear 2 funciones nuevas con el sostenido y el dacaeimiento para que me devuelvan una lista con los valores aplicandoles la función correspondiente de ataque, sostenido y bajada.
        """
        """
        Concateno las listas del ataque, caida y sonido y a eso lo multiplico por el wave.
        Luego eso es lo que tengo que devolver.
        NOTA: Fijate si no funciona, probar con un for.
        """
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