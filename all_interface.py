import os
import subprocess
import glob

def all_interface(inp, output):

    #home = 'C:/Users/ivanm/Desktop/projects/python/practica2/test/'
    home = inp[0:-5]# 'C:/Users/ivanm/Desktop/projects/python/practica2/mixed/'

    # songs = glob.glob('C:/Users/ivanm/Desktop/projects/python/practica2/mixed/*.wav')
    songs = glob.glob(inp)

    for my_song in songs:
        print(my_song)

        my_command = ['python', 'inference.py', '--input', home +
                       os.path.basename(my_song)[0:-4] + '.wav']

        subprocess.Popen(my_command, shell=True).wait()

    need_songs = glob.glob('./*_Instruments.wav')
    dont_need_songs = glob.glob('./*_Vocals.wav')

    for yes, no in zip(need_songs, dont_need_songs):
        print(yes[2:], no[2:])
        os.remove(no)
        os.replace(yes, output + yes[2:-16] + '.wav')


if __name__ == '__main__':
    all_interface('C:/Users/ivanm/Desktop/projects/python/practica2/mixed/*.wav',
                  'C:/Users/ivanm/Desktop/projects/python/practica2/fon_new_1min/')
