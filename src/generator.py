import os
import random
import mido

class Generator:
    """Class that generates the new music track.
    Attributes:
        trie: trie data structure class
        parser: midi parser class
        track: full note sequence for the generated track
    """

    def __init__(self):
        self.trie = None
        self.parser = None
        self.track = []

    def set_trie(self, trie):
        """Sets trie for music generation.
        Args:
            trie: trie data structure class
        """

        self.trie = trie

    def set_parser(self, parser):
        """Sets parser for music generation.
        Args:
            parser: midi parser class
        """

        self.parser = parser

    def generate(self, degree, midi_file, duration_mode, instrument):
        """Function that combines all the necessary steps for generating music.
        Args:
            degree: degree for generation chosen by the user
            midi_file: training data for generation chosen by the user
            duration_mode: mode for note durations chosen by the user
            instrument: instrument for the generated track chosen by the user
        """

        self.trie.set_degree(degree)
        self.parser.set_file(midi_file)

        data = self.parser.parse_notes()
        self.parser.parse_durations()

        self.trie.create_trie(data)

        initial_sequence = self.generate_initial_sequence()
        self.generate_new_sequence(initial_sequence)
        self.create_midi_file(duration_mode, instrument)

    def generate_initial_sequence(self):
        """Creates the first sequence of notes.
        Returns:
            initial_sequence: first notes (length of the degree)
        """

        initial_sequence = []
        degree = self.trie.degree
        current = self.trie.root

        for i in range(degree):
            next_notes = list(current.children.keys())
            counters = [current.children[note].counter for note in next_notes]

            total_count = sum(counters)
            probabilities = [count / total_count for count in counters]

            chosen_note = random.choices(next_notes, probabilities)[0]
            initial_sequence.append(chosen_note)
            self.track.append(chosen_note)
            current = current.children[chosen_note]
        return initial_sequence

    def generate_new_sequence(self, sequence):
        """Generates the rest of the track.
        Args:
            sequence: the sequence to base the next note on
        """

        if len(self.track) > 300:
            return self.track

        current = self.trie.root
        sequence.pop(0)

        for note in sequence:
            if note not in current.children:
                continue
            current = current.children[note]

        next_notes = list(current.children.keys())
        counters = [current.children[note].counter for note in next_notes]

        total_count = sum(counters)
        probabilities = [count / total_count for count in counters]

        chosen_note = random.choices(next_notes, probabilities)[0]
        self.track.append(chosen_note)
        sequence.append(chosen_note)

        self.generate_new_sequence(sequence)

    def create_midi_file(self, duration_mode, instrument, filename="generatedtrack.mid",
                        dir="src/GeneratedTracks"):
        """Creates the midi file for generated track.
        Args:
            duration_mode: mode for note durations
            instrument: instrument for the generated music
            filename: name for the generated track
            dir: path for the generated track
        """

        midi_file = mido.MidiFile(ticks_per_beat=self.parser.ticks_per_beat)
        track = mido.MidiTrack()
        midi_file.tracks.append(track)
        instrument_dict = {
            "Piano": 0,
            "Violin": 40,
            "Acoustic Guitar": 24,
            "Bagpipe": 109,
            "Saxophone": 65,
            "Bird Tweet": 123
        }
        program_number = instrument_dict.get(instrument)
        track.append(mido.Message('program_change', program=program_number))

        if duration_mode == "Same duration for every note":
            for note in self.track:
                on_message = mido.Message('note_on', note=note, velocity=100, time=0)
                off_message = mido.Message('note_off', note=note, velocity=100, time=150)
                track.append(on_message)
                track.append(off_message)

        if duration_mode == "Same durations as in source MIDI file":
            for note, duration in zip(self.track, self.parser.durations):
                on_message = mido.Message('note_on', note=note, velocity=100, time=0)
                off_message = mido.Message('note_off', note=note, velocity=100, time=duration)
                track.append(on_message)
                track.append(off_message)

        if duration_mode == "Randomized durations based on bars in source MIDI file":
            for note, duration in zip(self.track, self.parser.randomized_durations):
                on_message = mido.Message('note_on', note=note, velocity=100, time=0)
                off_message = mido.Message('note_off', note=note, velocity=100, time=duration)
                track.append(on_message)
                track.append(off_message)

        midi_file.save(os.path.join(dir, filename))
