############################################################################
# A sample program to create a single-track MIDI file, add a note,
# and write to disk.
############################################################################

#Import the library
from midiutil.MidiFile3 import MIDIFile


MyMIDI = MIDIFile(1)

# Add track name and tempo. The first argument to addTrackName and
# addTempo is the time to write the event.
track = 0
time = 0
channel = 9
MyMIDI.addTrackName(track,time,"Sample Track")
MyMIDI.addTempo(track,time, 120)

time = time = 2
MyMIDI.addProgramChange(0,channel, time, 44)    # voice 1 = 86   fretless bass
# Add a note. addNote expects the following information:

pitch = 60
duration = 10
volume = 100
duration2 = 5

# Now add the note.
MyMIDI.addNote(track,channel,pitch,time,duration,volume)
time = time + 1
MyMIDI.addNote(track,channel,pitch,time,duration,volume)
time = time + 1.25
MyMIDI.addNote(track,channel,pitch,time,duration,volume)
time = time + .5
MyMIDI.addNote(track,channel,pitch,time,duration,volume)
time = time + .5
MyMIDI.addNote(track,channel,pitch,time,duration,volume)


# And write it to disk.
binfile = open("outputLong.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()

