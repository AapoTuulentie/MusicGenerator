# Implementation
There are three main classes in src: MidiParser that is responsible for parsing the notes and durations from source MIDI, Trie which creates the trie data structure and Generator which generates the actual track and forms a new MIDI file for it.

## Trie
Music generation in the application is based on a trie data structure. The user chooses a sequence length n and all n-sequences and their frequencies will be stored in the trie. The sequence length is essentially connected to the degree of the Markov chain.

## Markov Chain
Markov chain's degree is always sequence length n-1. If the user decides to have 3 as sequence length, then the generation will be done with a second degree Markov chain, meaning that a new note is always picked based on 2 previous notes. Trie has a counter for each sequence that counts all occurences of notes in the source MIDI file. Probabilities for each sequence are calculated based on their frequency and the Markov chain process picks new notes based on them. 

## UI 
The application has a user interface that makes it easier to generate new tracks. The user has options to choose sequence length n, source MIDI file, duration mode and instrument. 
