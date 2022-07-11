from pydub import AudioSegment
import glob, os


def split_audio(inp, output):

    files = glob.glob(inp)
    for i, el in enumerate(files):
        t1 = 0  # Works in milliseconds
        t2 = 5000
        flag = 1
        counter = 1
        print('Working on file.....', el)
        newAudio = AudioSegment.from_wav(el)
        count = 1
        while flag:
            if t2 > len(newAudio):
                flag = 0
            else:
                nwAudio = newAudio[t1:t2]

                chunk_name = (os.path.basename(el)[0:-4]+ '_' + str(count) + ".wav")
                print(chunk_name)
                count += 1
                nwAudio.export(os.path.join(output, chunk_name), format="wav")
                t1 += 5000
                t2 += 5000
                counter += 1


if __name__ == '__main__':
        split_audio('./fon_new_1min', './fon_new_5sec')
