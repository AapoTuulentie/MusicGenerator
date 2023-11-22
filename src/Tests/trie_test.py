import unittest
from trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie(3)

    def test_root_has_children(self):
        data = [70, 74, 77, 70, 75, 79, 82, 77]
        self.trie.create_trie(data)
        root = self.trie.root
        self.assertTrue(root.children)

    def test_create_trie(self):
        data = [1, 2, 3]
        self.trie.create_trie(data)
        expected = "Note: 1, Counter: 1, Leaf: False\n  Note: 2, Counter: 1, Leaf: False\n    Note: 3, Counter: 1, Leaf: True\n"
        self.assertEqual(str(self.trie), expected)

    def test_no_duplicate_children(self):
        data = [70, 74, 77, 70, 75, 79, 82, 77]
        self.trie.create_trie(data)
        keys = list(self.trie.root.children.keys())
        self.assertEqual(keys, [70, 74, 77, 75, 79])