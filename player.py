from miditime.miditime import MIDITime
mymidi = MIDITime(120, 'music.mid')
midinotes = [
    [0, 60, 127, 3],
    [10, 61, 127, 4],
    [20, 63, 120, 5]
]
mymidi.add_track(midinotes)
mymidi.save_midi()
