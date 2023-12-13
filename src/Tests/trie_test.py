import unittest
from trie import Trie
from midi_parser import MidiParser

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.parser = MidiParser()
        self.trie.set_degree(3)
        testfile = 'src/Tests/Testfiles/bach_(trio)-sonatas_525_(c)harfesoft.mid'
        self.parser.set_file(testfile)
        self.testdata = self.parser.parse_notes()

    def test_root_has_children(self):
        data = [70, 74, 77, 70, 75, 79, 82, 77]
        self.trie.create_trie(data)
        root = self.trie.root
        self.assertTrue(root.children)

    def test_no_duplicate_children(self):
        data = [70, 74, 77, 70, 75, 79, 82, 77]
        self.trie.create_trie(data)
        keys = list(self.trie.root.children.keys())
        self.assertEqual(keys, [70, 74, 77, 75, 79])

    def test_add_sequence_to_trie(self):
        seq = [1, 2, 3]
        self.trie.add_sequence_to_trie(seq)
        trie = self.trie.display()
        expected = [([1, 2, 3], 1)]
        self.assertEqual(trie, expected)

    def test_all_sequences_are_in_trie(self):
        data = [1, 2, 3, 2, 3]
        self.trie.create_trie(data)
        trie = self.trie.display()
        expected = [([1, 2, 3], 1), ([2, 3, 2], 1), ([3, 2, 3], 1)]
        self.assertEqual(trie, expected)

    def test_counters_work_correctly(self):
        data = [1, 2, 3, 1, 2, 3]
        self.trie.create_trie(data)
        seq = self.trie.get_sequences_starting_from_note(1)
        expected = [([1, 2, 3], 2)]
        self.assertEqual(seq, expected)

    def test_with_min_degree(self):
        self.trie.set_degree(2)
        self.trie.create_trie(self.testdata)
        check = True
        trie = self.trie.display()
        for seq in trie:
            if len(seq[0]) == 2:
                continue
            else:
                check = False
                break
        self.assertTrue(check)

    def test_with_max_degree(self):
        self.trie.set_degree(9)
        self.trie.create_trie(self.testdata)
        check = True
        trie = self.trie.display()
        for seq in trie:
            if len(seq[0]) == 9:
                continue
            else:
                check = False
                break
        self.assertTrue(check)
        
