
############################################################################
# A  program read a data file of midi instrument values, generate another  file of midi instrument constants
# for specific languages and write to disk. This one is for Python 
############################################################################

#Import the library
from midiutil.MidiFile3 import MIDIFile

import csv

completeL = ""

f = open("Midi_DrumKit_Output.txt")
for row in csv.reader(f):
    completeL = completeL + row[1] + " = " + row[2] + "\n"


headerfile = open("DrumKitHeader.py", 'w')
headerfile.write(completeL)
headerfile.close()