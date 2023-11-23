#### Weekly Report 4
- UI is now at the point where it necessarily does not need to be further modified (only if I have time at some point)
- The running of the program moved to app.py and I created a generate-function that handles everything related to generating music
- All user inputs are now working correctly
- I had to do separate set-functions for all classes because otherwise back-to-back music generation without closing the app did not work
- Third duration mode is working: it takes sequences of bar-length durations, puts them in a list and randomizes them. The generated music does not sound that good though, I'm guessing it could be caused by changing time signatures
- Testing is updated and coverage is in the [testing document](https://github.com/AapoTuulentie/MusicGenerator/blob/main/Documentation/Testing_document.md). It is still lacking.
- Did not look into pylint yet

Next I will have to improve testing and apply pylint. Player for the generated track would also be nice in UI.  
