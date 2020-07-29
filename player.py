from miditime.miditime import MIDITime
mymidi = MIDITime(552, 'music.mid')
note_lenth = 3
notes = ['C4', 'C4', 'G4', 'C4', 'G#4', 'C4', 'G4', 'C4', 'G#3', 'G#3', 'D#4', 'F4', 'G3', 'G3', 'D4', 'D#4']
pitches = {
    'C3'  : 48,
    'C#3' : 49,
    'D3'  : 50,
    'D#3' : 51,
    'E3'  : 52,
    'F3'  : 53,
    'F#3' : 54,
    'G3'  : 55,
    'G#3' : 56,
    'A3'  : 57,
    'A#3' : 58,
    'B3'  : 59,
    'C4'  : 60,
    'C#4' : 61,
    'D4'  : 62,
    'D#4' : 63,
    'E4'  : 64,
    'F4'  : 65,
    'F#4' : 66,
    'G4'  : 67,
    'G#4' : 68,
    'A4'  : 69,
    'A#4' : 70,
    'B4'  : 71,
    'C5'  : 72
}
midinotes = []
time = 0
i = 0
for note in notes:
    midinotes.append([time, pitches[notes[i]], 127, note_lenth])
    i += 1
    time += note_lenth
mymidi.add_track(midinotes)
mymidi.save_midi()