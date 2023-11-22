class Node:
    def __init__(self):
        self.children = {}
        self.leaf = False
        self.counter = 0

class Trie:
    def __init__(self):
        self.root = Node()
        self.degree = None

    def set_degree(self, degree):
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
                node.counter += 1
            node.leaf = True

    def __str__(self):
        return self.display(self.root, 0)

    def display(self, node, level):
        result = ""
        for note, child_node in node.children.items():
            result += "  " * level + f"Note: {note}, Counter: {child_node.counter}, Leaf: {child_node.leaf}\n"
            result += self.display(child_node, level + 1)
        return result


    
















