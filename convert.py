import json

name = input('Enter song name:\n')
bpm = int(input('Enter bpm:\n'))
note_length = int(input('Enter length of notes:\n'))

notes = []
i = 0
cycle = True
ret = False
print('Enter notes (e.g. C#4), to return to previos note enter "return":\n')

while cycle == True:
    note = input()
    if not note == 'return' and not note == 'end':
        if ret:
            notes[i] = note
            ret = False
        else:
            notes.append(note)
        i += 1
    elif note == 'return':
        i -= 1
        ret = True
    elif note == 'end':
        cycle = False

song = {
    "name" : name,
    "bpm"  : bpm,
    "note_length" : note_length,
    "notes" : notes
}
with open('songs.json', 'r') as file:
    songs = json.load(file)

songs.append(song)

with open('songs.json', 'w') as file:
    json.dump(songs, file, sort_keys=True, indent=2)