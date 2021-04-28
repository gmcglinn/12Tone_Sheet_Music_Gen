tl;dr - run: python3 twelveTone.py
	input: whatever you'd like
	outputs: .ly file based on your inputs
	run: .ly file through lilypond
	done


Howdy! You're reading the readme for my final project for MAT320. This is
based on the chapter 6 topic of "12-Tone Music Composition" which takes
a predetermined 12 tone string of notes and uses various algorithms to 
transform itself into various similarily dissident phrases. The book goes
over:


Transposing
	Increasing each note in the tone row by a determined number of semitones.

Inverting
	In a sense flipping the tone row on its head, by making the highest
	tones the lowests, and second highest second lowest etc etc.

Retrograding
	This is reversing the tone row, so it plays the notes backwards.

Cyclic Shift
	Shifting each tone over a 'space', so the first played tone is now the
	second played tone, and the second the third etc. The 12th tone
	becomes the first tone.

Inverted Retrograde
	This is where you invert and retrograde the tone row (see above).

Prime
	Though not technically a transformation, I make note that this is
	the official name for an unmolested tone row.


This program here will take in a user input tone row (as well as other
various user inputs), and proceed to write a simple orchestral piece
that is 8 variations on the tone row long. For each of these variations, it
will randomly select a transformation method listed above (prime inc.) and
proceed to write it into a .ly file. There is also an "outputs" file that is
kinda a debug file that goes over each transformation as it happens
per instrument. To actually run the program, you should run "twelveTone.py" 
in your favorite python3 environment (MUST be python3 since I use tkinter).

My program here expects the user to have installed the program "lilypond", 
which is a kind of "translator" for what is coming out of my program. If
you take a peek into a created ly file, you will see it has "ais fis e". This
is what lilypond is expecting to see and translates over to notes on a staff
(in our case here it would be A# F# E).

I'm running a linux machine, so simply by trying to run lilypond (via command
line) will prompt an installation, on a windows/osx machine simply Google up
"Lilypond" and download from the official website (free!). I cannot speak on
the UI provided as I have never used them before, but it should just take in
a .ly file and output a PDF similar to my demonstration.


Thanks for reading this readme and I hope this program suffices for a decent 
grade! It's been a great semester and I've really loved attending this class.


Thanks,
Geoff




===Note from the program author=== 

I wish I was able to both:

A - find a way to produce sound based on the output file. I believe lilypond
is able to output a midi file, but given the time I had to work with it I
wasn't able to fully utilize lilypond. This segues into B...

B - I wish I could have made a more complicated algorithm for the actual
composition other than just quarter notes. As I began working, I noticed
I had to pretty much learn an entire new language in lilypond. This
hampered my ability to fully implement everything I wanted to (seen quite
obviously in my "range" variable declarations within the program haha). I
was also taken aback by just how difficult it is to get computers to make
listenable music that isn't just repetitive, so I would definitely say I
bit off more than I could chew by overpromising early on.
