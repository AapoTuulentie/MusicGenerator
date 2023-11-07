import mido

class MidiParser:
    def __init__(self, filename):
        self.filename = filename
        self.tempo = None
        self.ticks_per_beat = None

    def parse(self):
        file = mido.MidiFile(self.filename)
        data = []
        track_count = 0
        for track in file.tracks:
            track_data = []
            track_count += 1
            for msg in track:
                if msg.type == 'note_on':
                    note = msg.note
                    duration = msg.time
                    velocity = msg.velocity
                    data.append((note))
        return data

    def form_dict(self, data, degree):
        nodes_dict = {}
        previous = 0

        if degree == 1:
            for note in data:
                nodes_dict[note] = []
            for note in reversed(data):
                nodes_dict[note].append(previous)
                previous = note
        else:
            for i in range(len(data)):
                if i+degree < len(data):
                    key = str(data[i:i+degree])
                    nodes_dict[key] = []
            for i in range(len(data)-degree):
                key = str(data[i:i+degree])
                nodes_dict[key].append(data[i+degree])     
        return nodes_dict

if __name__ == "__main__":
    filename = '/home/aapotuul/MusicGenerator/Midi/bach_(trio)-sonatas_525_(c)harfesoft.mid'
    parser = MidiParser(filename)
    data = parser.parse()
    
    data2 = [43, 46, 46, 39, 39, 51, 51, 61, 61, 51, 51, 60, 60, 51, 51, 58, 58, 51, 51, 56, 56, 51, 51, 55, 55, 51, 51, 56, 56, 55, 55]
    print(parser.form_dict(data2,1))