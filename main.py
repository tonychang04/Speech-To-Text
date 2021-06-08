import sounddevice as sd
from scipy.io.wavfile import write

def record(soundpath):
    fs = 44100  # free-air resonant frequency
    seconds = 5  # first use prefixed time

    myrecording = sd.rec(int(seconds * fs), samplerate = fs, channels = 1)
    sd.wait() # wait until the recording is done
    write(soundpath,fs, myrecording)

# main method
if __name__ == '__main__':

    soundpath = 'output.wav'
    record(soundpath)




