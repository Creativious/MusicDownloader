This part of the program is basically the same as the before one in the above directory, but this one takes a voice input of a song name, can only do one song, not a playlist.

Just use the run.bat file and then say your song you want and it'll play it.

Also so that playback is faster, if the song is already downloaded it'll play that instead of downloading it though it still uses wifi to check the song title and compare it to the local file.

The search.py program just searches youtube and then sends back all results, main.py detects what is said and grabs the first result from the search.
musicgrabber.py does basically the same, but some functions are modified to interact with main.py better, such as outputing the audio_path to be played instead of the time elapsed.
It also detects if the song has been downloaded before and removes the playlist function almost completely, though is still there in some remnants.

Message Creativious#0874 on discord for more info