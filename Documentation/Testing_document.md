# Testing
Testing uses Bach's Trio Sonata 525 in C-major as a test file.

## About Testing
In this application, testing the output is difficult because creativity is not necessarily something that can be defined. The quality of the output depends on how good it sounds musically, which is subjective. If the musical aspects were to be tested, it would be most logical to do it as a survey with real people. What can be tested is, for example, whether the generated track follows the rules set by the user.

## Tests
Tests for the class MidiParser focus on testing that the notes and durations are correct in the parsed lists. The functionality in MidiParser is really simple so there is not much to test.

Tests for Trie class test that the trie is formed correctly. They ensure that
- All sequences from the source MIDI are stored in the trie
- Counters for each sequence are correct
- Sequences have the correct length
- Edge cases work (lowest and highest degree)

Test for Generator class test that forming the new track works correctly. This includes 
- Sequence length is correct
- Amount of notes in the track is correct
- The sequences in the generated track exist in source MIDI
- New file is created succesfully
- The generated track has the correct instrument and durations

## Quality of the Music
The source MIDI file needs to be 



Current coverage:

![image](https://github.com/AapoTuulentie/MusicGenerator/assets/101823904/5cefadf6-9405-4302-b5f6-9b6275b61a4c)
