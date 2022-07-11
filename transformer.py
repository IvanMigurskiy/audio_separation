import os
import subprocess
import glob
from flac_to_wav import flac_to_wav
from my_split_audio import my_split_audio
from summ_audio import summ_audio
from all_interface import all_interface
from split_audio import split_audio
from wav_to_png import wav_to_png

home = 'C:/Users/ivanm/Desktop/projects/python/practica2/music/'
directories = [[['voice/*.flac', "voice_wav"], ['fon/*.flac', "fon_wav"]],
               [['voice_wav/*.wav', "voice_1min"], ['fon_wav/*.wav', "fon_1min"]],
               [['voice_1min/*.wav', "fon_1min/*.wav", "mixed"]],
               [['mixed/*.wav', "fon_new_1min/"]],
               [['fon_new_1min/*.wav', "fon_new_5sec"], ['fon_1min/*.wav', "fon_5sec"]]]#,
               #[['fon_new_5sec/*.wav', "fon_new_png/"], ['fon_5sec/*.wav', "fon_png/"]]]
funcs = [flac_to_wav, my_split_audio, summ_audio, all_interface, split_audio]#, wav_to_png]

for func, my_dir in zip(funcs, directories):
    for d in my_dir:
        if func != summ_audio:
            func(home+d[0], home+d[1])
        else:
            func(home + d[0], home + d[1], home+d[2])
