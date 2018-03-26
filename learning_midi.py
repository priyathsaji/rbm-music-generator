import midi
import midi_manipulation as mm
import numpy as np





#pattern = midi.read_midifile("try.mid")
notestatematrix = mm.midiToNoteStateMatrix("Pop_Music_Midi/Around The World - Chorus.midi")

count = 0;
for track in notestatematrix:
	count+=1
	print(len(track))

print(count)
"""
statematrix = mm.midiToNoteStateMatrix("Pop_Music_Midi/All The Small Things - Chorus.midi")

span = 78

statematrix = np.array(statematrix)

if not len(statematrix.shape) == 3:

    statematrix = np.dstack((statematrix[:, :span], statematrix[:, span:]))

statematrix = np.asarray(statematrix)

pattern = midi.Pattern()

track = midi.Track()
pattern.append(track)

   
tickscale = 55

    

lastcmdtime = 0

prevstate = [[0,0] for x in range(span)]
for time, state in enumerate(statematrix + [prevstate[:]]):


mm.noteStateMatrixToMidi(statematrix)
pattern = midi.read_midifile("example.mid")
count = 0
for track in pattern:
	for i in track:
		count+=1
	print(track)

print(count)

for i in mm.midiToNoteStateMatrix("Pop_Music_Midi/All The Small Things - Chorus.midi"):
	print(i)
"""