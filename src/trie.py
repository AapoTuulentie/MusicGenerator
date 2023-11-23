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
        root: first node object in trie, not a note but rather it includes all "root" notes as children
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

        root = self.root
        for i in range(len(data) - self.degree+1):
            n_sequence = data[i:i+self.degree]
            node = root
            for n in n_sequence:
                if n not in node.children:
                    node.children[n] = Node()
                node = node.children[n]
                node.counter += 1
            node.leaf = True

    def __str__(self):
        """Returns the trie in a readable form"""

        return self.display(self.root, 0)

    def display(self, node, level):
        """Creates a display of the trie structure.
        Args:
            node: root node
            level: determines node placement in display based on how far it is from root
        """

        result = ""
        for note, child_node in node.children.items():
            result += "  " * level + f"Note: {note}, Counter: {child_node.counter}, Leaf: {child_node.leaf}\n"
            result += self.display(child_node, level + 1)
        return result


    
















