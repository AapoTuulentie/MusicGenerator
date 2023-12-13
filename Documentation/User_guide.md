# User Guide
This project uses Poetry.
## Download
Install Poetry. Clone the repository for the latest version.

## Installation & startup

Install dependencies with

```bash
poetry install
```

Run the application with

```bash
poetry run invoke start
```

## Usage
There are 4 different fields in the music generation page:

- **Select Sequence Length (n):** These are the options for sequence length n. All of the n-sequences from source data are saved in the trie. The degree of the Markov chain is n-1, so for example in music generation if you choose a sequence length of 3, the Markov chain will choose a new note based on the 2 previous notes.

- **Select Source MIDI File:** This will set the source data.

- **Select Note Duration Mode:** This will determine the way note durations are generated. The options for this are
  - **Same durations for every note:** This will set the same duration for each note
  - **Same durations as in source MIDI file:** This will copy the note durations from the source data and apply them to your new generated MIDI
  - **Randomized durations based on bars in source MIDI file:** This will randomize durations in the source MIDI and generate new patterns that are the length of a bar

- **Select Instrument:** This will set the instrument for the generated MIDI.

Src has two folders for MIDI files: **Midi** and **GeneratedTracks**. Midi includes all source MIDI files. GeneratedTracks will include the generated music in the file **generatedtrack.mid**.


## Testing

Run tests with

```bash
poetry run invoke test
```

Get test coverage with

```bash
poetry run invoke coverage
```

Get Pylint score with

```bash
poetry run invoke pylint
```
