import sounddevice as sd
from scipy.io.wavfile import write

def record():
    fs = 44100  # free-air resonant frequency
    seconds = 5  # first use prefixed time

    myrecording = sd.rec(int(seconds * fs), samplerate = fs, channels = 2)
    sd.wait() # wait until the recording is done
    write('output.wav',fs, myrecording )

# main method
if __name__ == '__main__':
    record()




