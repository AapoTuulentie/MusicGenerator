from collections import defaultdict

from midi_parser import MidiParser

class Node:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self, degree):
        self.root = Node()
        self.degree = degree

    def form_trie(self, data):
        node = self.root
        for i in range(len(data) - self.degree):
            notes = data[i:i + self.degree]
            child = data[i + self.degree]

            if tuple(notes) not in node.children:
                new_node = Node()
                node.children[tuple(notes)] = [new_node]
            else:
                node.children[tuple(notes)][0].children[tuple([child])] = []

            node = new_node
            

if __name__ == "__main__":
    filename = '/home/aapotuul/MusicGenerator/Midi/bach_(trio)-sonatas_525_(c)harfesoft.mid'
    parser = MidiParser(filename)
    data = parser.parse()
    data2 = [47, 47, 53, 53, 51, 51, 50, 50, 48, 48, 52, 52, 41, 41, 49, 49, 48, 48]
    t = Trie(3)
    t.form_trie(data2)

    


    



    
















