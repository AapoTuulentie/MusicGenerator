## Implementation
#### Trie
Music generation in the application is based on a trie data structure. 

#### Markov Chain
Trie has a counter for each node that counts all occurences of notes in the source MIDI file. With these counters, the generation mechanism is able to calculate possibilities for notes appearing after certain sequences and uses a Markov chain to generate a new note sequence. 

#### UI 
The application has a user interface that makes it easier to change generation settings. 