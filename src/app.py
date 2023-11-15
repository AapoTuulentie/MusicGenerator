from midi_parser import MidiParser
from trie import Trie
from generator import Generator

def main():
    parser = MidiParser()
    trie = Trie(3)
    generator = Generator(trie, parser)


if __name__ == "__main__":
    main()