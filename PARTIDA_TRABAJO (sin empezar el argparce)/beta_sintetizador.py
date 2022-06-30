#%%
import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
import threading 
#hará que me reproduzca dos notas al mismo tiempo
import pyaudio
import wave 
from notes import dic_notes

"""El sounddivice me permitira reproducir una onda sonora"""
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

def music_debussy(filename):
    with open(filename,"r") as debussy:
        list_1 = []
        for line in debussy:
            line = line.strip()
            list_2 = line.split(" ")
            list_2 = tuple(list_2)
            list_1.append(list_2)
        list_notes = []
        for one,two,three in list_1:
            list_notes.append(two)
        
        return list_notes

if __name__=="__main__":
    clas_c = Sound()
    #note_A0 = clas_c.dic_notes["A0"]
    #note_A4 = clas_c.dic_notes["A4"]
    #note_C2 = clas_c.dic_notes["C2"]
    #note_A4 = clas_c.dic_notes["A4"]
    #lista = [note_A0,note_A4,note_C2]
    #clas_c.play_chord(lista)
    lista = music_debussy("debussy_note.txt")
    notes = []
    for i in lista:
        note_music = clas_c.dic_notes[i]
        notes.append(note_music)
    frames = []
    for note in notes:
        print(note)
        sonido = clas_c.play(note,1,44100)
        onda = clas_c.create_data(note,1,44100)
        frames.append(onda)
    print(frames)
    
    hunk = 1024  
    
    chunk = 1024  
  
    sample_format = pyaudio.paInt16   
    chanels = 2
  
    smpl_rt = 44100 #44400
    #seconds = 4
    filename = "audio.wav"
    
    pa = pyaudio.PyAudio()   
  
    pa.terminate() 

    print('Terminó') 
  
    sf = wave.open(filename, 'wb') 
    sf.setnchannels(chanels) 
    sf.setsampwidth(pa.get_sample_size(sample_format)) 
    sf.setframerate(smpl_rt) 
    sf.writeframes(b''.join(frames)) 
    sf.close()
    











