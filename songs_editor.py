import json

def create():
    with open('songs.json', 'r') as file:
        songs = json.load(file)

    for song in songs:
        if song['name'] == 'Every breath you take':
            notes = []
            for note in song['notes']:
                if note[0] == 'PAUSE':
                    notes.append([note[0], 1/16])
                else:
                    notes.append([note[0], song['note_length']])
            song['notes'] = notes

    with open('songs.json', 'w') as file:
        json.dump(songs, file, sort_keys=True, indent=2)
    print('File has been rewrited!')

print('Your songs file may be destroyed')
if input('Do you understend? (Y)es/(N)o:\n') == 'Y':
    create()
else:
    print('Abort, abort!')
input('Press Enter to exit...')