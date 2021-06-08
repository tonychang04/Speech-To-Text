import sounddevice as sd
import speech_recognition as sr

from scipy.io.wavfile import write


def record(soundpath):
    fs = 44100  # free-air resonant frequency
    seconds = 5  # first use prefixed time

    myrecording = sd.rec(int(seconds * fs), samplerate = fs, channels = 1)
    sd.wait() # wait until the recording is done
    write(soundpath,fs, myrecording)

def convertSpeech(soundpath):
    r = sr.Recognizer()
    with sr.AudioFile(soundpath) as source:
        audio_text = r.listen(source)

    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        # using google speech recognition
        text = r.recognize_google(audio_text)
        print('Converting audio transcripts into text ...')
        print(text)

    except:
        print('Sorry.. run again...')

# main method
if __name__ == '__main__':

    soundpath = 'output.mp3'
    record(soundpath)
    convertSpeech(soundpath)



