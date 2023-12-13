import random
import mido

class MidiParser:
    """Class that parses the training data.
    Attributes:
        filename: training data file
        durations: parsed note durations from midi
        randomized_durations: randomized parsed note duration sequences that are the length of a bar
        ticks_per_beat: number of ticks in each quarter note in the training data
    """

    def __init__(self):
        self.filename = None
        self.durations = []
        self.randomized_durations = []
        self.ticks_per_beat = None

    def set_file(self, file):
        """Sets the training data file.
        Args:
            file: midi file chosen by the user
        """

        self.filename = file

    def parse_notes(self):
        """Parses notes from the tracks of the training data and returns them as a list.
        Returns:
            notes: parsed notes
        """

        file = mido.MidiFile(self.filename)
        self.ticks_per_beat = file.ticks_per_beat
        notes = []
        track_count = 0
        for track in file.tracks:
            track_count += 1
            for msg in track:
                if msg.type == 'note_on':
                    if msg.velocity == 0 or msg.time == 0:
                        continue
                    note = msg.note
                    notes.append(note)
        return notes

    def parse_durations(self):
        """Parses durations from training data and adds them to self.durations.
        Also creates self.randomized_durations"""

        file = mido.MidiFile(self.filename)
        patterns = []
        beats_per_bar = 4
        combined_durations = 0
        single_bar = []

        for track in file.tracks:
            for msg in track:
                if msg.type == 'note_on':
                    duration = msg.time
                    if duration < 20 or duration > 2000:
                        continue
                    self.durations.append(duration)
                    single_bar.append(duration)
                    combined_durations += duration
                    if combined_durations >= self.ticks_per_beat * beats_per_bar:
                        patterns.append(single_bar)
                        single_bar = []
                        combined_durations = 0
        random.shuffle(patterns)
        for pattern in patterns:
            for duration in pattern:
                self.randomized_durations.append(duration)
