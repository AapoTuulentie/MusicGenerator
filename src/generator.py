from trie import Trie
from midi_parser import MidiParser
import random
import mido

class Generator:
    def __init__(self, trie, parser):
        self.trie = trie
        self.parser = parser
        self.track = []

    def generate_initial_sequence(self):
        initial_sequence = []
        degree = self.trie.degree
        current = self.trie.root

        for i in range(degree):
            next_notes = list(current.children.keys())
            counters = [current.children[note].counter for note in next_notes]
            
            total_count = sum(counters)
            probabilities = [count / total_count for count in counters]

            chosen_note = random.choices(next_notes, probabilities)[0]
            initial_sequence.append(chosen_note)
            self.track.append(chosen_note)
            current = current.children[chosen_note]
        return initial_sequence
    
    def generate_new_sequence(self, sequence):
        if len(self.track) > 300:
            return self.track
        
        current = self.trie.root
        sequence.pop(0)

        for note in sequence:
            if note not in current.children:
                continue
            current = current.children[note]

        next_notes = list(current.children.keys())
        counters = [current.children[note].counter for note in next_notes]
        
        total_count = sum(counters)
        probabilities = [count / total_count for count in counters]

        chosen_note = random.choices(next_notes, probabilities)[0]
        self.track.append(chosen_note)
        sequence.append(chosen_note)

        self.generate_new_sequence(sequence)

    def create_midi_file(self, filename="generatedtrack.mid"):
        midi_file = mido.MidiFile(ticks_per_beat=self.parser.ticks_per_beat)
        track = mido.MidiTrack()
        midi_file.tracks.append(track)
        track.append(mido.Message('program_change', program=104))
        for note, duration in zip(self.track, self.parser.durations):
            on_message = mido.Message('note_on', note=note, velocity=100, time=0)
            off_message = mido.Message('note_off', note=note, velocity=100, time=duration) 
            track.append(on_message)
            track.append(off_message)

        midi_file.save(filename)

    
if __name__ == "__main__":
    filename = '/home/aapotuul/MusicGenerator/Midi/aatbak.mid'
    filename2 = '/home/aapotuul/MusicGenerator/Midi/bach_(trio)-sonatas_525_(c)harfesoft.mid'
    filename3 = '/home/aapotuul/MusicGenerator/Midi/ty_november.mid'
    parser = MidiParser(filename3)
    data = parser.parse_notes()
    data2 = [1,2,3,4,4,5,5,3,2,2,3,1,2,3,4,3,2,5,3,2]
    durations = parser.parse_durations()
    t = Trie(3)
    x = Generator(t, parser)

    t.create_trie(data)
    print(t)

    f = x.generate_initial_sequence()
    x.generate_new_sequence(f)
    print(x.track)
    x.create_midi_file(filename="generatedtrack.mid")
    print(len(x.track))
