import unittest
import os
import mido
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
        self.assertEqual(len(self.generator.track), 501)

    def test_sequences_exist_in_training_data(self):
        initial_sequence = self.generator.generate_initial_sequence()
        self.generator.generate_new_sequence(initial_sequence.copy())
        root = self.trie.root
        sequences_exist = True

        for i in range(len(self.generator.track) - self.trie.degree + 1):
            seq = self.generator.track[i:i + self.trie.degree]
            current = root
            for note in seq:
                if note not in current.children:
                    sequences_exist = False
                    break
                current = current.children[note]
            if not sequences_exist:
                break

        self.assertTrue(sequences_exist)

    def test_created_file_exists(self):
        initial_sequence = self.generator.generate_initial_sequence()
        self.generator.generate_new_sequence(initial_sequence.copy())
        duration_mode = "Same duration for every note"
        instrument = "Piano"
        testfile_path = "src/Tests/Testfiles/test_output.mid"

        self.generator.create_midi_file(duration_mode, instrument, filename="test_output.mid",
                                        dir="src/Tests/Testfiles/")
        self.assertTrue(os.path.exists(testfile_path))

    def test_generated_file_has_correct_instrument_and_durations(self):
        initial_sequence = self.generator.generate_initial_sequence()
        self.generator.generate_new_sequence(initial_sequence.copy())
        testfile_path = "src/Tests/Testfiles/test_output.mid"
        instrument = "Bird Tweet"
        duration_mode = "Same duration for every note"
        self.generator.create_midi_file(duration_mode, instrument, filename="test_output.mid",
                                        dir="src/Tests/Testfiles/")
        self.assertTrue(os.path.exists(testfile_path))

        midi_file = mido.MidiFile(testfile_path)

        expected = 123
        instrument_number = midi_file.tracks[0][0].program
        self.assertEqual(instrument_number, expected)

        correct = True
        for track in midi_file.tracks:
            for msg in track:
                if msg.type == "note_on":
                    if msg.time == 0 or 150:
                        continue
                    correct = False
                    break
        self.assertTrue(correct)

    def tearDown(self):
        testfile_path = "src/Tests/Testfiles/test_output.mid"
        if os.path.exists(testfile_path):
            os.remove(testfile_path)
