from pydub import AudioSegment
import glob, os

def summ_audio(vc, fn, mx):

    fons = glob.glob(fn)
    voices = glob.glob(vc)

    #lst = zip(fons, voices[0:len(fons)])
    i = 1

    for fon, voice in zip(fons, voices):

        sound1 = AudioSegment.from_wav(fon)
        sound2 = AudioSegment.from_wav(voice)

        sound3 = sound1.overlay(sound2, position=0)

        chunk_name = (os.path.basename(fon)[0:-4] + ".wav")
        i += 1
        print("in summ exporting", chunk_name)
        sound3.export(
            os.path.join(mx, chunk_name),
            format="wav")



if __name__ == '__main__':
    summ_audio('./fon_1min/*.wav', './voice_1min/*.wav', "./mixed")
