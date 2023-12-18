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
The most unique melodies are generated with the "Randomized durations" mode, where durations are randomized by bars. It can be quite random at times with the durations going from slow to fast suddenly, but overall they are alright. The tick rate is always the same as in source MIDI, so some tracks are faster than others, for example the Bach's Trio Sonata. When the sequence length is around 6 or above, the resemblance starts to be noticeable with the source MIDI.

I noticed that best sounding unique generated tracks are generated with sequence length 3 or 4 and randomized durations. Still, I would not call these musical pieces particuralry "good" sounding but they seem to be in the right key and at times they produce short snippets of a good melody.

## Coverage

Test coverage:

![image](https://github.com/AapoTuulentie/MusicGenerator/assets/101823904/32bd0119-75d3-4977-8683-d8be09400784)

Coverage is a bit lower for the class Generator because it holds a main type function generate, which is not directly tested. 

## Pylint

![image](https://github.com/AapoTuulentie/MusicGenerator/assets/101823904/46327373-8dd6-4ad2-b2fa-fedc739e10f5)



