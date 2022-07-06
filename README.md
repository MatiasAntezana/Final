# Synthetizer 

This repository contains a Python packgage that allows reading a musical score and synthetize the musical notes in diferent envelope shapes from the use of diferents mathematicals functions and sound modulalization or configuration of musical instruments. This creates a WAVE file that can be reproduced with some music player. 
Also it can be used a musical score and send notes to play on a real intrument, a robotic xilophone that receives the notes from the program and can play the music.  


--------------------------------

## Installation

To use this library you must execute the following instructions:

1. Clone the repository.
$ git clone https://github.com/MatiasAntezana/Final.git

2. Get in the local repository.
   
   cd/path/to/final   

3. Install the dependencies
   
   pip install -r requirements.txt

4. Install it setup with pip
   
   pip install .

--------------------------------

## Running the program

To run the program you need to run the following command:

1. Get in the local repository.
   
   cd/path/to/final 

2. Enter to the main menu program.
   
   python menu.py -h

--You will see the arguments that are required

3. Choose frequency, instrument, score, and the name for the WAV file.
   
   python menu.py --f=<frequency.> --i=<instrument.txt> --s=<note.txt> --a=<audio_test.wav>


--------------------------------

## Tests

To run the python tests from the packgage you can use the following command:

   python -m unittest discover

