import unittest
from midi_parser import MidiParser

class TestMidiParser(unittest.TestCase):
    def setUp(self):
        testfile = 'src/Tests/Testfiles/bach_(trio)-sonatas_525_(c)harfesoft.mid'
        self.parser = MidiParser()
        self.parser.set_file(testfile)

    def test_parse_notes(self):
        notes = self.parser.parse_notes()
        first_10 = notes[:10]
        expected = [70, 74, 77, 70, 75, 79, 82, 77, 75, 74]
        self.assertEqual(first_10, expected)

    def test_notes_amount_correct(self):
        notes = self.parser.parse_notes()
        amount = len(notes)
        self.assertEqual(amount, 4487)

    def test_parse_durations(self):
        self.parser.parse_notes()
        self.parser.parse_durations()
        first_10 = self.parser.durations[:10]
        expected = [70, 26, 70, 26, 142, 50, 70, 26, 70, 26]
        self.assertEqual(first_10, expected)