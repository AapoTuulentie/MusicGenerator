import unittest
from trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.data = [49, 49, 49, 46, 51, 51, 50, 50, 48, 48, 52, 52, 41, 41, 49, 49, 49, 49]
        self.trie = Trie(3)

    def test_root_has_children(self):
        self.trie.create_trie(self.data)
        root = self.trie.root
        self.assertTrue(root.children)

    