from midinotes import MIDInotes
import json, os, sys, time as clock

if not os.path.exists('./songs'):
    os.mkdir('./songs')

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
instrument = int(input('Enter instrument number (e.g. Piano - 1, Overdr. Guitar - 30):\n')) - 1

for i in range(repeats):
    note_list.extend(song['notes'])

with open('pitches.json', 'r') as file:
    pitches = json.load(file)
midinotes = []
time = 0
toolbarwide = 50 #len(note_list)
i = 0

print('[{}]'.format('-' * toolbarwide), end = '', flush = True)

for note in note_list:
    i += 1
    progress = round(i / len(note_list) * 50)
    sys.stdout.write('\b' * (toolbarwide + 1))
    print('[' + '#' * progress, end = '', flush = True)
    clock.sleep(0.01)
    if not note[0] == 'PAUSE':
        midinotes.append([time, pitches[note[0]], 127, note[1]])
    time += note[1]
    
mymidi = MIDInotes(tempo = song['bpm']*2, outfile = f'./songs/{song["name"]}.mid')
mymidi.add_track(midinotes)
mymidi.save_midi(instrument)
print(f'\nTrack saved as {song["name"]}.mid in song folder.')
os.system(os.path.abspath(f'./songs/"{song["name"]}.mid"'))
input('Press Enter to exit...')