from trie import Trie
from midi_parser import MidiParser
import random

class Generator:
    def __init__(self, trie):
        self.trie = trie
        self.velocity = 100

    def generate_sequence(self):
        new_sequence = []
        degree = self.trie.degree
        first_note = list(self.trie.root.children.keys())
        return first_note

    def pick_note(self, note):
        for c in self.trie.root.children[note]:
            print(c)

# KESKEN
        
        
    


if __name__ == "__main__":
    filename = '/home/aapotuul/MusicGenerator/Midi/bach_(trio)-sonatas_525_(c)harfesoft.mid'
    parser = MidiParser(filename)
    data = parser.parse_notes()
    data2 = [49, 49, 49, 46, 51, 51, 50, 50, 48, 48, 52, 52, 40, 40, 39, 40, 40, 50]
    t = Trie(2)
    x = Generator(t)
    t.create_trie(data2)
    print(t)
    print(t.generate_random_sequence())
    print(x.generate_sequence())