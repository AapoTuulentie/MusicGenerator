import mido

class MidiParser:
    def __init__(self, filename):
        self.filename = filename
        self.durations = []
        self.ticks_per_beat = None
        
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
    filename = '/home/aapotuul/MusicGenerator/Midi/bach_(trio)-sonatas_525_(c)harfesoft.mid'
    filename2 = '/home/aapotuul/MusicGenerator/Midi/aatbak.mid'
    filename3 = '/home/aapotuul/MusicGenerator/Midi/ty_november.mid'
    parser = MidiParser(filename3)
    notes = parser.parse_notes()
    durations = parser.parse_durations()
    data2 = [43, 46, 46, 39, 39, 51, 51, 61, 61, 51, 51, 60, 60, 51, 51, 58, 58, 51, 51, 56, 56, 51, 51, 55, 55, 51, 51, 56, 56, 55, 55]

    print(durations)
    print(len(notes))
    print(len(durations))
    print(sum([70, 26, 70, 26, 142, 50, 70, 26, 70, 26, 238]))