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
        "1": 31,
       # "1.5": 45,
        "2": 38,
      #  "2.5": 50,
         "3": 43,
      #  "3.5": 50,
        "4": 38,
      #  "4.5":45
    }
    return switcher.get(argument, 0)    

def weatherevent_to_values(argument):
    switcher = {
        "1": 77,
        "2": 116,
        "3": 47,
        "4": 45,
        "5": 112,
        "6": 54,
        "7": 55
    }
    return switcher.get(argument, 0)  
    
    
def randompitch():
    
    pitcher = randint(0,3)
    return pitcher
        
    
# constant values
channel = 0
channel2 = 1
channel3 = 2

channel10 = 9
    
track1 = 0
track2 = 1
track3 = 2
time = 0

beats = 800

# indexes to elements of data row
windDirection = 7
windSpeed = 6
precipitation = 1
yearColumn = 4
weatherColumn = 8
weatherYear = "1950"
stormCenter = 1

pitch = 60
highTempAdjustment = 30
lowTempAdjustment = 30

# Create the MIDIFile Object with 3 tracks plus names of tracks

MyMIDI = MIDIFile(3)
MyMIDI.addTrackName(track1,time,"Year Changes")
time = time +1
MyMIDI.addTrackName(track2,time,"Percussion")
time = time +1
#MyMIDI.addTrackName(track3,time,"Misc")
#time = time +1
MyMIDI.addTempo(track1,time, beats)
time = time +1
MyMIDI.addTempo(track2,time, beats)
#time = time +1
#MyMIDI.addTempo(track3,time, beats)

# set voice (sound) to be played on tracks
#  we used General Midi sounds ( see General Midi docs )
time = time +1
MyMIDI.addProgramChange(track1,channel, time, 12)    # voice 1 = 86   fretless bass
#time = time +1
#MyMIDI.addProgramChange(track2,channel10, time, 40)    # voice 2 = 53
#time = time +1
#MyMIDI.addProgramChange(track3,2, time, 77)   # cymbal = 119

time = time +1

# open and read each line ( data object ) in file
f = open("StormyWeather.txt")
for row in csv.reader(f):
    
    # calculate pitch value from temperatures
    #pitch1 =  20 + winddirection_to_values(row[windDirection])
    
    
    dingaLing = 1
    duration = 1.5
    durationlong = .5
    volume = 80  
    
   
    if row[yearColumn] != weatherYear:  
        MyMIDI.addNote(track1,channel,45,time,durationlong,volume)     
        
    weatherYear = row[yearColumn]     
    
    tim = time + 1

    
    #pitch1 =   moonphase_to_values(row[moonphase])  
    #pitch2Tmp = float(row[windSpeed]) 
   # pitch2 = int(pitch2Tmp) + lowTempAdjustment
   
    stormCenter = weatherevent_to_values(row[weatherColumn]) 
    
    pitch = 60 + randompitch()
    time = time +1
    MyMIDI.addProgramChange(track2,channel2, time, stormCenter)
    time = time +1
    MyMIDI.addNote(track2,channel2,pitch,time,durationlong,volume) 
    
    time = time +1
   # MyMIDI.addNote(track2,channel2,pitch2,time,duration,volume)
   # time = time + 1
   # if row[precipitation] != "0.00":  #got some rain today
   #     pitch3 = 64 + randompitch()
    #    pitch4 = pitch3 + 4
     #   MyMIDI.addNote(track3,channel3,pitch3,time,1,100) 
      #  MyMIDI.addNote(track3,channel3,pitch4,time,1,100) 
       # pitch3 = pitch3 + 1
       # MyMIDI.addNote(track3,channel3,pitch3,time,3,100)        
    #print(row[1])


time = time + 2

# change track 3 to ocean sound for the finale !!

#MyMIDI.addProgramChange(track3,2, time, 122)   # 122 = Seashore
#time = time + 1
#MyMIDI.addNote(track3,channel3,40,time,45,100) # let it ring....


# And write it to disk.
binfile = open("1950- SevereWeather.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()



