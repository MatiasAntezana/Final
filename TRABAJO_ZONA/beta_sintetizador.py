import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np

"""El sounddivice me permitira reproducir una onda sonora"""
def g_frequency(note,octave):
    expo = (octave - 4) * 12 + (note - 10)
    """Note = Nota"""
    """Me dirá que tan fuerte se tiene que escuchar el sonido"""
    return 440 * ((2**(1/12))** expo)

def play(note,octave):
    framerate = 44100
    time = 1000
    frequency = g_frequency(note,octave)
    t = np.linspace(0,time/1000)
    wave = np.sin(2*np.pi * frequency * t)
    print(len(t))
    plt.plot(wave[:1000])
    plt.show()
    sd.play(wave,framerate)
    sd.wait()

for note in range (1,13):
    play(note,3)













