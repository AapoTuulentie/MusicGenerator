import tkinter as tk
import os
from tkinter import ttk
from generator import Generator
from midi_parser import MidiParser
from trie import Trie

class Ui:
    """Class that creates an user interface for the application.
    Attributes:
        root: tkinter root
        menu_frame: frame for the menu
        generation_frame: frame for the generation page
        trie: class trie that is set in different function
        parser: class parser that is set in different function
        generator: class generator that is set in different function
    """

    def __init__(self):
        self.root = tk.Tk() 
        self.root.title("MusicGenerator") 
        self.root.geometry("800x600")
        self.menu_frame = None
        self.generation_frame = None
        self.trie = None
        self.parser = None
        self.generator = None

    def create_initial_components(self):
        """Creates new objects for trie, parser and generator everytime a new file is generated"""

        self.trie = Trie()
        self.parser = MidiParser()
        self.generator = Generator()

    def run(self):
        """Runs UI loop"""
        self.menu()
        self.root.mainloop()

    def menu(self):
        """Creates menu that opens when the app is ran"""

        self.menu_frame = tk.Frame(self.root, padx=20, pady=20)
        self.menu_frame.pack(expand=True)

        font = ("Courier", 20)
        welcome_label = tk.Label(self.menu_frame, text="Welcome to Music Generator", font=font)
        welcome_label.pack(pady=20)

        start_button = tk.Button(self.menu_frame, text="Start", font=font, command=self.generation_page)
        start_button.pack()

    def generation_page(self):
        """Generation page where user can choose generation settings"""

        self.menu_frame.destroy()
        self.generation_frame = tk.Frame(self.root, padx=20, pady=20)
        self.generation_frame.pack(expand=True)

        degree_label = tk.Label(self.generation_frame, text="Select Degree\n(length of a sequence)", font=("Courier", 12))
        degree_label.pack(pady=10)

        degree_values = [str(i) for i in range(2, 10)]
        degree_var = tk.StringVar()
        degree_dropdown = ttk.Combobox(self.generation_frame, textvariable=degree_var, values=degree_values, width=10)
        degree_dropdown.pack(pady=10)
        degree_dropdown.set(degree_values[0])

        midi_label = tk.Label(self.generation_frame, text="Select Source MIDI File", font=("Courier", 12))
        midi_label.pack(pady=10)

        midi_folder_path = 'src/Midi'
        midi_files = [file for file in os.listdir(midi_folder_path) if file.endswith('.mid')]
        midi_var = tk.StringVar()
        midi_dropdown = ttk.Combobox(self.generation_frame, textvariable=midi_var, values=midi_files, width=45)
        midi_dropdown.pack(pady=10)
        if midi_files:
            midi_dropdown.set(midi_files[0])

        duration_label = tk.Label(self.generation_frame, text="Select Note Duration Mode", font=("Courier", 12))
        duration_label.pack(pady=10)

        duration_modes = ["Same duration for every note", "Same durations as in source MIDI file", "Randomized durations based on bars in source MIDI file"]
        duration_var = tk.StringVar()
        duration_dropdown = ttk.Combobox(self.generation_frame, textvariable=duration_var, values=duration_modes, width=45)
        duration_dropdown.pack(pady=10)
        duration_dropdown.set(duration_modes[0])

        instrument_label = tk.Label(self.generation_frame, text="Select Instrument", font=("Courier", 12))
        instrument_label.pack(pady=10)

        instruments = ["Piano", "Violin", "Acoustic Guitar", "Bagpipe", "Saxophone", "Bird Tweet"]
        instrument_var = tk.StringVar()
        instrument_dropdown = ttk.Combobox(self.generation_frame, textvariable=instrument_var, values=instruments, width=20)
        instrument_dropdown.pack(pady=10)
        instrument_dropdown.set(instruments[0])

        generate_button = tk.Button(self.generation_frame, text="Generate Music", font=("Courier", 16), command=lambda: self.generate_music(degree_var.get(), midi_var.get(), duration_var.get(), instrument_var.get()))
        generate_button.pack(pady=20)

    def generate_music(self, degree, midi_file, duration_mode, instrument):
        """Function that passes user input values to generators generate-function
        Args:
            degree: length of a sequence in generation
            midi_file: midi file to use as training data
            duration_mode: determines how the length of notes is generated
            instrument: which instrument is used in the generated track
        """

        degree = int(degree)
        midi_folder_path = 'src/Midi'
        midi_file_path = os.path.join(midi_folder_path, midi_file)
        self.create_initial_components()
        self.generator.set_trie(self.trie)
        self.generator.set_parser(self.parser)
        
        self.generator.generate(degree, midi_file_path, duration_mode, instrument)