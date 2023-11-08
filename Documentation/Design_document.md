## Design Document
MusicGenerator is meant to be an application for generating musical compositions using a Markov chain algorithm. It should take existing musical data, process it and use a Markov chain to create new sequences.
#### Algorithm Design
Data parsing algorithms receive a MIDI-file as input and construct a parsed list of attributes, such as notes, note durations and note velocities. After that a trie data structure is formed and a Markov chain algorithm will generate note sequences. User will be able to control the length of a sequence in the trie, which changes the degree of the Markov chain. For example, if the degree is 2, the next note will be picked based on the current note and the note before that.
Time complexity for a second-degree Markov chain algorithm would be O(n³), with n being the number of states.
#### Data Structures
The application uses a trie data structure. The maximum length of a sequence in the trie is defined by the user. All note sequences from the training data will be saved in the trie.

###### Aapo Tuulentie, Bachelor of Computer Science
###### Programming language: Python
###### Known programming languages: Python
###### Language: English