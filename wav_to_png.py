import os
import matplotlib
import matplotlib.pyplot as plt
import pylab
import librosa
import librosa.display
import numpy as np
import glob, os
from PIL import Image


def wav_to_png(inp, output):

    songs = glob.glob(inp)

    for my_song in songs:
        chunk_name = (output + os.path.basename(my_song)[0:-4] + ".png")
        print(chunk_name)

        sig, sr = librosa.load(my_song)
        S = librosa.feature.melspectrogram(y=sig, sr=sr)

        fig, ax = plt.subplots()

        S_dB = librosa.power_to_db(S, ref=np.max)
        img = librosa.display.specshow(S_dB, sr=sr, fmax=8000, ax=ax)
        #fig.colorbar(img, ax=ax)

        plt.imsave(fname=chunk_name, arr=S_dB, cmap='inferno', format='png')
        plt.close(fig)


if __name__ == '__main__':
        wav_to_png('./fon_new_5sec/*.wav', "./fon_new_png/")


'''
songs = glob.glob('./fon_new_5sec/*.wav')
songs = glob.glob('./test/*.wav')

for my_song in songs:
    chunk_name = ("./fon_new_png/" + os.path.basename(my_song)[0:-4] + ".png")
    print(chunk_name)

    sig, fs = librosa.load(my_song)
    S = librosa.feature.melspectrogram(y=sig, sr=fs)
    #plt = librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
    pylab.show()
    #img = Image.fromarray(S)

    #img.show()

    #plt.imsave(fname=chunk_name, arr=img, cmap='inferno', format='png')
'''


'''
songs = glob.glob('./fon_new_5sec/*.wav')
songs = glob.glob('./test/*.wav')

for my_song in songs:
    sig, fs = librosa.load(my_song)
    # make pictures name
    chunk_name = ("./fon_new_png/" + os.path.basename(my_song)[0:-4] + ".png")
    print(chunk_name)

    pylab.axis('off') # no axis
    pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[]) # Remove the white edge
    S = librosa.feature.melspectrogram(y=sig, sr=fs)
    #plt = librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
    #pylab.savefig(chunk_name, bbox_inches=None, pad_inches=0)
    plt.imsave(fname=chunk_name, arr=S, cmap='inferno', format='png')

    pylab.close()
'''