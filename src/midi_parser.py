import mido

class MidiParser:
    def __init__(self):
        self.filename = None
        self.durations = []
        self.ticks_per_beat = None
        
    def set_file(self, file):
        self.filename = file

    def parse_notes(self):
        file = mido.MidiFile(self.filename)
        self.ticks_per_beat = file.ticks_per_beat
        notes = []
        track_count = 0
        for track in file.tracks:
            track_count += 1
            for msg in track:
                if msg.type == 'note_on':
                    if msg.velocity == 0 or msg.time == 0:
                        continue
                    note = msg.note
                    notes.append(note)
        return notes

    def parse_durations(self):
        file = mido.MidiFile(self.filename)
        for track in file.tracks:
            for msg in track:
                if msg.type == 'note_on':
                    duration = msg.time
                    if duration == 0:
                        continue
                    self.durations.append(duration)
        return self.durations


if __name__ == "__main__":
    parser = MidiParser()
    filename = '/home/aapotuul/MusicGenerator/Midi/bach_(trio)-sonatas_525_(c)harfesoft.mid'
    parser.set_file(filename)
    durations = parser.parse_durations()
    print(durations)