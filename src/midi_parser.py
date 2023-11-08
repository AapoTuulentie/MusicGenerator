import mido

class MidiParser:
    def __init__(self, filename):
        self.filename = filename
        self.tempo = None
        self.ticks_per_beat = None

    def parse_notes(self):
        file = mido.MidiFile(self.filename)
        notes = []
        track_count = 0
        for track in file.tracks:
            track_count += 1
            for msg in track:
                if msg.type == 'note_on':
                    note = msg.note
                    duration = msg.time
                    velocity = msg.velocity
                    notes.append(note)
        return notes

    def parse_durations(self):
        file = mido.MidiFile(self.filename)
        durations = []
        for track in file.tracks:
            for msg in track:
                if msg.type == 'note_on':
                    duration = msg.time
                    durations.append(duration)
        return durations


if __name__ == "__main__":
    filename = '/home/aapotuul/MusicGenerator/Midi/bach_(trio)-sonatas_525_(c)harfesoft.mid'
    parser = MidiParser(filename)
    notes = parser.parse_notes()
    durations = parser.parse_durations()
    data2 = [43, 46, 46, 39, 39, 51, 51, 61, 61, 51, 51, 60, 60, 51, 51, 58, 58, 51, 51, 56, 56, 51, 51, 55, 55, 51, 51, 56, 56, 55, 55]
    print(notes)
    print(durations)