class Node:
    """Class that creates a node object for the trie class.
    Attributes:
        children: dictionary that includes all children of a node
        leaf: if current node is the last of a sequence
        counter: counts how many times a note appears in the same position
    """

    def __init__(self):
        self.children = {}
        self.leaf = False
        self.counter = 0

class Trie:
    """Class that creates a trie data structure consisting of node objects.
    Attributes:
        root: first node object in trie
        degree: length of a sequence
    """

    def __init__(self):
        self.root = Node()
        self.degree = None

    def set_degree(self, degree):
        """Sets the degree for trie creation.
        Args:
            degree: degree from user input
        """

        self.degree = degree

    def create_trie(self, data):
        """Creates the actual trie structure.
        Args:
            data: a list of parsed midi data from midi parser
        """

        for i in range(len(data) - self.degree+1):
            sequence = data[i:i+self.degree]
            self.add_sequence_to_trie(sequence)

    def add_sequence_to_trie(self, sequence):
        """Adds a single sequence to the trie
        Args:
            sequence: single sequence of notes to be added to the trie
        """

        node = self.root
        for n in sequence:
            if n not in node.children:
                node.children[n] = Node()
            node = node.children[n]
            node.counter += 1
        node.leaf = True

    def get_sequences_starting_from_note(self, start_note):
        """Returns all sequences starting from the given note.
        Args:
            start_note: the note from which the sequences start
        Returns:
            sequences: list of sequences that start from the given note
        """

        sequences = []
        display_result = self.display()

        for sequence, counter in display_result:
            if sequence[0] == start_note:
                sequences.append((sequence, counter))
        return sequences

    def display(self, node=None):
        """Returns a list of tuples where each tuple includes (sequence as a list, counter).
        Args:
            node: root node (default is None, starts from the root of the trie)
        Returns:
            trie: the whole trie as a list of tuples
        """

        if node is None:
            node = self.root
        trie = []

        for note, child_node in node.children.items():
            if child_node.leaf:
                sequence = [note]
                trie.append((sequence, child_node.counter))
            else:
                sub_sequences = self.display(child_node)
                for sub_sequence, counter in sub_sequences:
                    trie.append(([note] + sub_sequence, counter))
        return trie
