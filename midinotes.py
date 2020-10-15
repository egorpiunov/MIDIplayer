from midiutil.MidiFile3 import MIDIFile

class MIDInotes(object):

    def __init__(self, tempo=120, outfile='midi.mid'):
        self.tempo = tempo
        self.outfile = outfile
        self.tracks = []

    def add_track(self, note_list):
        self.tracks.append(note_list)

    def add_note(self, track, channel, note):
        time = note[0]
        pitch = note[1]
        velocity = note[2]
        duration = note[3]

        # Now add the note.
        self.MIDIFile.addNote(track, channel, pitch, time, duration, velocity)

    def save_midi(self, instrument):
        # Create the MIDIFile Object with 1 track
        self.MIDIFile = MIDIFile(len(self.tracks))
        #self.MIDIFile.addProgramChange(0, 0, 0, instrument)

        for i, note_list in enumerate(self.tracks):

            # Tracks are numbered from zero. Times are measured in beats.
            track = i
            time = 0

            # Add track name, tempo and instrument change event
            self.MIDIFile.addTrackName(track, time, "Track %s" % i)
            self.MIDIFile.addTempo(track, time, self.tempo)
            self.MIDIFile.addProgramChange(track, 0, time, instrument)

            for n in note_list:
                if len(n) == 2:
                    note = n[0]
                    channel = n[1]
                else:
                    note = n
                    channel = 0
                self.add_note(track, channel, note)

        # And write it to disk.
        with open(self.outfile, 'wb') as binfile:
            self.MIDIFile.writeFile(binfile)
