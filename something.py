import midi
import numpy as np

pattern = midi.read_midifile("Pop_Music_Midi/All The Small Things - Chorus.midi")
timeleft = [track[0].tick for track in pattern]
print(timeleft)
