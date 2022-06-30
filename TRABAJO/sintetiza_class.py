import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
import threading
#hará que me reproduzca dos notas al mismo tiempo (falta)
#import pyaudio
#import wave
"""El sounddivice me permitira reproducir una onda sonora"""
from notes import dic_notes

def combo (wave,t,d,t0):
    """
    Función que crea lo de ataque, sostenido y decaeimiento.
    Parametros:
    ----------
        t -> El t
        t0 -> Instante en el que comienza la nota
        d -> Duración de la nota
    """
    conta = 0
    lista = []
    for num in t:
        ta = 0.05 #intervalo de tiempo ataque
        td = 0.02 #intervalo de tiempo decrecimiento
        fa = np.sin((np.pi * num) / (2 * t0)) #función del ataque
        #print(fa)
        fs = 1 * num #funcion del sostenido
        fd = 1 - float(num / t0) #función del decaeimiento
        if t0 < num and num < t0 + ta:
            mt = fa * (num - t0)
            #print("si")
        elif (t0 + ta) < num and num < (t0 + d):
            mt = fs * float(t0 + d) * fd * float(num-(t0+d))
            #print("si")
        elif (t0 + d) < num and t < (t0 + d + td):
            mt = fs * (t0 + d) * fd * (num - (t0 + d))
            #print("si")
        else:
            mt = 0
            #print("no")
        A = 5 #instrumento
        at = A * wave[conta] * mt
        conta += 1
        lista.append(at)
    return lista

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
    
    """Si lo uso para el play, está de más"""

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
        framerate=44100"""
        t = np.linspace(0,time/1,int(time*framerate))
        wave = np.sin(2*np.pi * frequency * (t-t0))
        resultado = combo(wave,t,time,t0)
        #print(resultado)
        #print(t + t0)
        self.data = wave
        #print(self.data)
        """
        Tengo que crear 2 funciones nuevas con el sostenido y el dacaeimiento para que me devuelvan una lista con los valores aplicandoles la función correspondiente de ataque, sostenido y bajada.
        """
        """
        Concateno las listas del ataque, caida y sonido y a eso lo multiplico por el wave.
        Luego eso es lo que tengo que devolver.
        NOTA: Fijate si no funciona, probar con un for.
        """
        
        #plt.plot(wave[:1000], color = 'k', label = 'Frecuencia de notas hz')
        #plt.title('Simulacro de notas')
        #plt.xlabel('Hz')
        #plt.ylabel('Variacion')
        #plt.legend(loc=3)
        #plt.show()
        
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