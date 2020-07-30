from miditime.miditime import MIDITime
import json
with open('songs.json') as file:
    songs = json.load(file)
    string = ''
    i = 0
    for song in songs:
        i += 1
        string += f'({i}) {song["name"]}.\n'
    song = songs[int(input('Choose song:\n' + string)) - 1]

note_list = []
repeats = int(input('Enter number of repeats:\n'))
for i in range(repeats):
    note_list.extend(song['notes'])

with open('pitches.json', 'r') as file:
    pitches = json.load(file)
midinotes = []
time = 0
for note in note_list:
    if not note[0] == 'PAUSE':
        midinotes.append([time, pitches[note[0]], 127, note[1]])
    time += note[1]
    
mymidi = MIDITime(song['bpm']*2, f'./songs/{song["name"]}.mid')
mymidi.add_track(midinotes)
mymidi.save_midi()
print(f'Track saved as {song["name"]}.mid in song folder.')
input('Press Enter to exit...')