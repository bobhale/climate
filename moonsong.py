############################################################################
# A sample program read a data file, generate a midi file
# and write to disk.
############################################################################

#Import the library
from midiutil.MidiFile3 import MIDIFile
from random import randint

import csv

def winddirection_to_values(argument):
    switcher = {
        "N": 19,
        "E": 23,
        "S": 26,
        "W": 27
    }
    return switcher.get(argument, 0)
    
def moonphase_to_values(argument):
    switcher = {
        "1": 43,
        "1.5": 45,
        "2": 46,
        "2.5": 50,
        "3": 52,
        "3.5": 50,
        "4": 46,
        "4.5":45
    }
    return switcher.get(argument, 0)    

def randompitch():
    
    pitcher = randint(0,3)
    return pitcher
        
    
# constant values
channel = 0
channel2 = 1
channel3 = 2
    
track1 = 0
track2 = 1
track3 = 2
time = 0

beats = 720

# indexes to elements of data row
windDirection = 7
windSpeed = 6
precipitation = 1
moonphase = 8

highTempAdjustment = 30
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
MyMIDI.addProgramChange(track1,0, time, 1)    # voice 1 = 86   fretless bass
#time = time +1
MyMIDI.addProgramChange(track2,1, time, 112)    # voice 2 = 53
time = time +1
MyMIDI.addProgramChange(track3,2, time, 73)   # cymbal = 119

time = time +1

# open and read each line ( data object ) in file
f = open("lunarprecipitation.txt")
for row in csv.reader(f):
    
    # calculate pitch value from temperatures
    #pitch1 =  20 + winddirection_to_values(row[windDirection])
        
    pitch1 =   moonphase_to_values(row[moonphase])  
    #pitch2Tmp = float(row[windSpeed]) 
   # pitch2 = int(pitch2Tmp) + lowTempAdjustment
    duration = 1.5
    durationlong = 2.0
    volume = 100  
    
    # add initial tracks
    # Add a note. addNote expects the following information:
    if row[moonphase] != "0":  
        MyMIDI.addNote(track1,channel,pitch1,time,durationlong,volume) 
    
    time = time +1
   # MyMIDI.addNote(track2,channel2,pitch2,time,duration,volume)
   # time = time + 1
    if row[precipitation] != "0.00":  #got some rain today
        pitch3 = 64 + randompitch()
        MyMIDI.addNote(track3,channel3,pitch3,time,1,100) 
       # pitch3 = pitch3 + 1
       # MyMIDI.addNote(track3,channel3,pitch3,time,3,100)        
    #print(row[1])


time = time + 4

# change track 3 to ocean sound for the finale !!

#MyMIDI.addProgramChange(track3,2, time, 122)   # 122 = Seashore
#time = time + 1
#MyMIDI.addNote(track3,channel3,40,time,45,100) # let it ring....


# And write it to disk.
binfile = open("2015MSPMoonPrecip.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()



