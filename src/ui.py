import tkinter as tk
import os
from tkinter import ttk
from generator import Generator
from midi_parser import MidiParser
from trie import Trie

class Ui:
    def __init__(self, trie, parser, generator):
        self.trie = trie
        self.parser = parser
        self.generator = generator
        self.root = tk.Tk() 
        self.root.title("MusicGenerator") 
        self.root.geometry("800x600")
        self.menu_frame = None
        self.generation_frame = None
        self.menu()

    def menu(self):
        self.menu_frame = tk.Frame(self.root, padx=20, pady=20)
        self.menu_frame.pack(expand=True)

        font = ("Courier", 20)
        welcome_label = tk.Label(self.menu_frame, text="Welcome to Music Generator", font=font)
        welcome_label.pack(pady=20)

        start_button = tk.Button(self.menu_frame, text="Start", font=font, command=self.generation_page)
        start_button.pack()

    def generation_page(self):
        self.menu_frame.destroy()
        self.generation_frame = tk.Frame(self.root, padx=20, pady=20)
        self.generation_frame.pack(expand=True)

        degree_label = tk.Label(self.generation_frame, text="Select Degree\n(length of a sequence the generation is based on)", font=("Courier", 12))
        degree_label.pack(pady=10)

        degree_values = [str(i) for i in range(1, 10)]
        degree_var = tk.StringVar()
        degree_dropdown = ttk.Combobox(self.generation_frame, textvariable=degree_var, values=degree_values, width=10)
        degree_dropdown.pack(pady=10)
        degree_dropdown.set(degree_values[0])

        midi_label = tk.Label(self.generation_frame, text="Select Source MIDI File", font=("Courier", 12))
        midi_label.pack(pady=10)

        midi_folder_path = 'src/Midi'
        midi_files = [file for file in os.listdir(midi_folder_path) if file.endswith('.mid')]
        midi_var = tk.StringVar()
        midi_dropdown = ttk.Combobox(self.generation_frame, textvariable=midi_var, values=midi_files, width=40)
        midi_dropdown.pack(pady=10)
        if midi_files:
            midi_dropdown.set(midi_files[0])

        duration_label = tk.Label(self.generation_frame, text="Select Note Duration Mode", font=("Courier", 12))
        duration_label.pack(pady=10)

        duration_modes = ["Same duration for every note", "Same durations as in source MIDI file"]
        duration_var = tk.StringVar()
        duration_dropdown = ttk.Combobox(self.generation_frame, textvariable=duration_var, values=duration_modes, width=40)
        duration_dropdown.pack(pady=10)
        duration_dropdown.set(duration_modes[0])

        generate_button = tk.Button(self.generation_frame, text="Generate Music", font=("Courier", 12), command=self.generate_music)
        generate_button.pack(pady=20)

if __name__ == "__main__":
    filename = '/home/aapotuul/MusicGenerator/Midi/ty_november.mid'
    trie = Trie(3)
    parser = MidiParser(filename)
    generator = Generator(trie, parser)

    ui = Ui(trie, parser, generator)
    ui.root.mainloop()