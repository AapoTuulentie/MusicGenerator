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
            print(track)
            track_count += 1
            for msg in track:
                if msg.type == 'note_on':
                    if msg.velocity == 0 or msg.time == 0:
                        continue
                    note = msg.note
                    notes.append(note)
        return notes

    def parse_durations_and_velocities(self):
        file = mido.MidiFile(self.filename)
        durations = []
        velocities = []
        for track in file.tracks:
            for msg in track:
                if msg.type == 'note_on':
                    duration = msg.time
                    velocity = msg.velocity
                    if duration > 500 or duration < 30:
                        continue
                    if velocity == 0:
                        continue
                    durations.append(duration)
                    velocities.append(velocity)
        return durations, velocities


if __name__ == "__main__":
    filename = '/home/aapotuul/MusicGenerator/Midi/bach_(trio)-sonatas_525_(c)harfesoft.mid'
    filename2 = '/home/aapotuul/MusicGenerator/Midi/aatbak.mid'
    parser = MidiParser(filename)
    notes = parser.parse_notes()
    durations = parser.parse_durations_and_velocities()
    data2 = [43, 46, 46, 39, 39, 51, 51, 61, 61, 51, 51, 60, 60, 51, 51, 58, 58, 51, 51, 56, 56, 51, 51, 55, 55, 51, 51, 56, 56, 55, 55]

    print(notes)
    print(durations)
    print(len(notes))
    print(len(durations))