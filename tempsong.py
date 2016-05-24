############################################################################
# A sample program read a data file, generate a midi file
# and write to disk.
############################################################################

#Import the library
from midiutil.MidiFile3 import MIDIFile

import csv

# constant values
channel = 0
channel2 = 1
channel3 = 2
    
track1 = 0
track2 = 1
track3 = 2
time = 0

beats = 540

# indexes to elements of data row
highTemp = 1
lowTemp = 2
precipitation = 3

highTempAdjustment = 20
lowTempAdjustment = 30

# Create the MIDIFile Object with 3 tracks plus names of tracks

MyMIDI = MIDIFile(3)
MyMIDI.addTrackName(track1,time,"Temperature MusicHI")
time = time +1
MyMIDI.addTrackName(track2,time,"Temperature MusicLOW")
time = time +1
MyMIDI.addTrackName(track3,time,"Temperature MusicPrecip")
time = time +1
MyMIDI.addTempo(track1,time, beats)
time = time +1
MyMIDI.addTempo(track2,time, beats)
time = time +1
MyMIDI.addTempo(track3,time, beats)

# set voice (sound) to be played on tracks
#  we used General Midi sounds ( see General Midi docs )
time = time +1
MyMIDI.addProgramChange(track1,0, time, 53)    # voice 1 = 53
time = time +1
MyMIDI.addProgramChange(track2,1, time, 53)    # voice 2 = 53
time = time +1
MyMIDI.addProgramChange(track3,2, time, 119)   # cymbal = 119

time = time +1

# open and read each line ( data object ) in file
f = open("climate2010.txt")
for row in csv.reader(f):
    
    # calculate pitch value from temperatures
    pitch1 = int(row[highTemp]) + highTempAdjustment
    pitch2 = int(row[lowTemp]) + lowTempAdjustment
    duration = .5
    volume = 100  
    
    # add initial tracks
    # Add a note. addNote expects the following information:
    MyMIDI.addNote(track1,channel,pitch1,time,duration,volume)
    time = time +1
    MyMIDI.addNote(track2,channel2,pitch2,time,duration,volume)
    time = time + 1
    if row[precipitation] != "0.00":  #got some rain today
        pitch3 = 96
        MyMIDI.addNote(track3,channel3,pitch3,time,3,90)        
    #print(row[1])


time = time + 4

# change track 3 to ocean sound for the finale !!

MyMIDI.addProgramChange(track3,2, time, 122)   # 122 = Seashore
time = time + 1
MyMIDI.addNote(track3,channel3,40,time,45,100) # let it ring....


# And write it to disk.
binfile = open("climatetemp2010_TempsPrecip.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()

