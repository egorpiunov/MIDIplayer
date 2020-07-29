from miditime.miditime import MIDITime
mymidi = MIDITime(120, 'music.mid')
notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C+1']
pitches = {
    'C' : 60,
    'D' : 62,
    'E' : 64,
    'F' : 65,
    'G' : 67,
    'A' : 69,
    'B' : 71,
    'C+1' : 72
}
midinotes = []
time = 0
i = 0
for note in notes:
    midinotes.append([time, pitches[notes[i]], 127, 2])
    i += 1
    time += 2
mymidi.add_track(midinotes)
mymidi.save_midi()
