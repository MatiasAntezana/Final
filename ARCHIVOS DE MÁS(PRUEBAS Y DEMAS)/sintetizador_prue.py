from notes import notes_mapping
import random
import thinkdsp
from pydub import AudioSegment
from pydub.playback import play
list_1 = []
for i in range (0, 8):
    list_1.append(random.uniform(-1,1))

list_2 = []

def Create (noteName = "A4", type = "sine", amp = 0.5, beats = 1.0, filter=None, cutoff = None, filename="default"):
    frecuency = notes_mapping[noteName]
    duration = beats / 2
    signal = thinkdsp.SinSignal(freq=0)

    for i in range(0,8):
        signal += thinkdsp.SinSignal(freq=frecuency*i, amp = 1, offset=0)

    wave = signal.make_wave(duration=duration, start = 0, fremerate = 44100)
    wave.write(filename=filename)
    audio = AudioSegment.from_wav(filename)

    if filter == "lowPass":
        audio = audio.low_pass_filter(cutoff)
    if filter == "highPass":
        audio = audio.high_pass_filter(cutoff)
    
    return audio
a4 = Create(noteName="A4", type = "sine" , amp=1.0, beats = 1.0, filter=None, cutoff=None)
play(a4)



