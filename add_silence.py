from pydub import AudioSegment
from pydub.playback import play
import os

add = '/home/nianheng/Documents/hiwi/01januar/fabian/Tense_Identificantion_Test/' \
      'recording_morphology_experiment/00results/old/'

out = '/home/nianheng/Documents/hiwi/01januar/fabian/Tense_Identificantion_Test/' \
      'recording_morphology_experiment/00results/stimuli/'
file_list = os.listdir(add)

silent_segment = AudioSegment.silent(duration=150)
for each in file_list:
    song = AudioSegment.from_wav(add+each)
    final_song = song + silent_segment
    final_song.export(out+each, format="wav")

