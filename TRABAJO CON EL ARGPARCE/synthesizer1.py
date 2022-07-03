
from synthesizer import Player, Synthesizer, Waveform



player = Player()
#player.open_stream()
synthesizer = Synthesizer(osc1_waveform=Waveform.sine, osc1_volume=1.0, use_osc2=False)
# Play A4
player.play_wave(synthesizer.generate_constant_wave(440.0, 3.0))

# Play C major
chord = ["C3", "E3", "G3"]
player.play_wave(synthesizer.generate_chord(chord, 3.0))

# You can also specify frequencies to play just intonation
chord = [440.0, 550.0, 660.0]
player.play_wave(synthesizer.generate_chord(chord, 3.0))

player.enumerate_device()
# index: 00, name: "Built-in Microphone", rate: 44100
# index: 01, name: "Built-in Output", rate: 44100
# index: 02, name: "UA-25EX 44.1kHz", rate: 44100
player.open_stream(device_name="UA-25EX")
