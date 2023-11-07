## Design Document
MusicGenerator is meant to be an application for generating musical compositions using a Markov chain algorithm. It should take existing musical data, process it and use a Markov chain to create new sequences.
#### Algorithm Design
Data collection and processing algorithms receive a MIDI-file as input and construct a Markov chain from the notes in the file. Attributes such as note sequences and durations are extracted. When a Markov chain is formed, a generator algorithm will generate new music based on probabilities in the chain. The goal is to try generating music with at least first- and second-order Markov chains. Second-order Markov chain needs to know the probability of transitioning to next state, considering the current and previous states.
Time complexity for a second-order Markov chain algorithm would be O(n³), with n being the number of states.
#### Data Structures
A Markov chain is a trie data structure and its creation will depend on which degree Markov chain the user wants to make. All the sequences will be saved in the trie depending on the degree.

###### Aapo Tuulentie, Bachelor of Computer Science
###### Programming language: Python
###### Known programming languages: Python
###### Language: English