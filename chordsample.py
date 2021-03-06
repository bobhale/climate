############################################################################
# A sample program to create a single-track MIDI file, add a note,
# and write to disk.
############################################################################

#Import the library
from midiutil.MidiFile3 import MIDIFile

import csv

track1 = 0
track2 = 1
time = 0

MyMIDI = MIDIFile(2)
MyMIDI.addTrackName(track1,time,"Temperature MusicHI")
time = time +1
MyMIDI.addTrackName(track2,time,"Temperature MusicLOW")
time = time +1
MyMIDI.addTempo(track1,time, 540)
time = time +1
MyMIDI.addTempo(track2,time, 540)

time = time +1
MyMIDI.addProgramChange(track1,0, time, 1)
time = time +1
MyMIDI.addProgramChange(track2,1, time, 2)

time = time +1

#f = open("climate2010.txt")
#for row in csv.reader(f):
    
channel = 0
channel2 = 1
pitch1 = 60
pitch2 = 64
duration = 5
volume = 100
time = time +2
MyMIDI.addNote(track1,channel,pitch1,time,duration,volume)
    #time = time +1
MyMIDI.addNote(track2,channel2,pitch2,time,duration,volume)
time = time + 2
MyMIDI.addNote(track1,channel,pitch1,time,duration,volume)
    #time = time +1
MyMIDI.addNote(track2,channel2,pitch2,time,duration,volume)
time = time + 2
MyMIDI.addNote(track1,channel,pitch1,time,duration,volume)
    #time = time +1
MyMIDI.addNote(track2,channel2,pitch2,time,duration,volume)
MyMIDI.addNote(track2,channel2,67,time,duration,volume)
    #print(row[1])
# Create the MIDIFile Object
# Now add the note.


#MyMIDI.addNote(track,channel,55,time,duration,volume)
#MyMIDI.addNote(track,channel,76,4,duration,volume)
#MyMIDI.addNote(track,channel,80,6,duration,volume)
# Add track name and tempo. The first argument to addTrackName and
# addTempo is the time to write the event.


# Add a note. addNote expects the following information:


# And write it to disk.
binfile = open("chordTemp.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()

