from pydub import AudioSegment
import subprocess
import glob, os


def flac_to_wav(inp, output):
    songs = glob.glob(inp)
    i = 1
    for my_song in songs:
        my_command = ['ffmpeg', '-i', inp[:-6] + os.path.basename(my_song), output + '/' + str(i) + ".wav"]
        subprocess.Popen(my_command, shell=True).wait()
        i += 1


if __name__ == '__main__':
    flac_to_wav('./music/fon/*.flac', "./music/fon_wav")
