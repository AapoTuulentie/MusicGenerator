from midi_parser import MidiParser
import random

class Node:
    def __init__(self):
        self.children = {}
        self.leaf = False

class Trie:
    def __init__(self, degree):
        self.root = Node()
        self.degree = degree

    def create_trie(self, data):
        root = self.root
        for i in range(len(data) - self.degree+1):
            n_sequence = data[i:i+self.degree]
            node = root
            for n in n_sequence:
                if n not in node.children:
                    node.children[n] = Node()
                node = node.children[n]
            node.leaf = True

# Function for testing purposes
    def generate_random_sequence(self):
        root = self.root
        sequence = []
        for _ in range(self.degree):
            children = list(root.children.keys())
            if root.leaf == True:
                break 
            random_child = random.choice(children)
            sequence.append(random_child)
            root = root.children[random_child]
        return sequence
    
    def __str__(self):
        return self.display(self.root, 0)

    def display(self, node, level):
        result = ""
        for note, child_note in node.children.items():
            result += "  " * level + f"Note: {note}, Leaf: {child_note.leaf}\n"
            result += self.display(child_note, level + 1)
        return result


if __name__ == "__main__":
    filename = '/home/aapotuul/MusicGenerator/Midi/bach_(trio)-sonatas_525_(c)harfesoft.mid'
    parser = MidiParser(filename)
    data = parser.parse_notes()
    data2 = [49, 47, 49, 46, 51, 51, 50, 50, 48, 48, 52, 52, 41, 41, 49, 49, 48, 48]
    t = Trie(4)
    t.create_trie(data2)
    print(t)
    random_sequence = t.generate_random_sequence()
    print("Random Sequence:", random_sequence)




    



    
















