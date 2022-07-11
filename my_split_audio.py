from pydub import AudioSegment
from pydub.utils import make_chunks
import glob, os


def my_split_audio(inp, output):
    songs = glob.glob(inp)
    count = 1
    for my_song in songs:
        song = AudioSegment.from_wav(my_song)
        chunk_length_ms = 60000  # pydub calculates in millisec
        chunks = make_chunks(song, chunk_length_ms)  # Make chunks of one sec

        # Export all of the individual chunks as wav files
        for i, chunk in enumerate(chunks):
            if count > 1:
                break


            if chunk.duration_seconds < 60:
                break
            chunk_name = (os.path.basename(my_song)[0:-4] + '_' + str(i+1) + ".wav")
            print("in my split exporting", chunk_name)
            #chunk.export(chunk_name, format="wav")
            chunk.export(os.path.join(output, chunk_name), format="wav")
            count += 1


if __name__ == '__main__':
    my_split_audio('./test/*.wav', "./test")
