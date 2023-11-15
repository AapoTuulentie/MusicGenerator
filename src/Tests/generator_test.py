import unittest
from generator import Generator
from midi_parser import MidiParser
from trie import Trie

class TestGenerator(unittest.TestCase):
    def setUp(self):
        testfile = 'src/Tests/Testfiles/bach_(trio)-sonatas_525_(c)harfesoft.mid'
        self.parser = MidiParser(testfile)
        data = self.parser.parse_notes()
        self.trie = Trie(3)
        self.trie.create_trie(data)
        self.generator = Generator(self.trie, self.parser)

    def test_generate_initial_sequence(self):
        initial_sequence = self.generator.generate_initial_sequence()
        self.assertEqual(len(initial_sequence), self.trie.degree)

    def test_generate_new_sequence(self):
        initial_sequence = self.generator.generate_initial_sequence()
        self.generator.generate_new_sequence(initial_sequence.copy())
        self.assertLessEqual(len(self.generator.track), 301)

    def test_create_midi_file(self):
        self.generator.generate_initial_sequence()
        self.generator.create_midi_file(filename="test_generated_track.mid")
        # Add assertions here to check if the file was created successfully
        # You might check if the file exists, its size, or if it follows the MIDI file format
