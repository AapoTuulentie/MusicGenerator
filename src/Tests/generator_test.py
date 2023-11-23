import unittest
import os
from generator import Generator
from midi_parser import MidiParser
from trie import Trie

class TestGenerator(unittest.TestCase):
    def setUp(self):
        self.testfile = 'src/Tests/Testfiles/bach_(trio)-sonatas_525_(c)harfesoft.mid'
        self.parser = MidiParser()
        self.parser.set_file(self.testfile)
        data = self.parser.parse_notes()

        self.trie = Trie()
        self.trie.set_degree(3)
        self.trie.create_trie(data)

        self.generator = Generator()
        self.generator.set_parser(self.parser)
        self.generator.set_trie(self.trie)

    def test_generate_initial_sequence(self):
        initial_sequence = self.generator.generate_initial_sequence()
        self.assertEqual(len(initial_sequence), self.trie.degree)

    def test_generate_new_sequence(self):
        initial_sequence = self.generator.generate_initial_sequence()
        self.generator.generate_new_sequence(initial_sequence.copy())
        self.assertLessEqual(len(self.generator.track), 301)

    def test_create_midi_file(self):
        initial_sequence = self.generator.generate_initial_sequence()
        self.generator.generate_new_sequence(initial_sequence.copy())
        duration_mode = "Same duration for every note"
        instrument = "Piano"
        testfile_path = "src/Tests/Testfiles/test_output.mid"

        self.generator.create_midi_file(duration_mode, instrument, filename="test_output.mid", dir="src/Tests/Testfiles/")
        self.assertTrue(os.path.exists(testfile_path))

    def tearDown(self):
        testfile_path = "src/Tests/Testfiles/test_output.mid"
        if os.path.exists(testfile_path):
            os.remove(testfile_path)


        