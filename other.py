import speech_recognition as sr
import argparse
import queue
import sys
import keyboard
import sounddevice as sd
import soundfile as sf
import os

from googletrans import Translator


def translate(speech):
    translator = Translator()
    word = translator.translate(speech, dest='zh-cn')
    print(word.text)
    return word.text


def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text


# referenced https://python-sounddevice.readthedocs.io/en/0.4.1/examples.html#recording-with-arbitrary-duration
def record_asynch(soundpath):
    """
    A method used to record the speech, will be terminated once user pressed r
    :param soundpath: the path of sound to be saved
    """
    if os.path.isfile(soundpath):
        os.remove(soundpath)

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument(
        '-l', '--list-devices', action='store_true',
        help='show list of audio devices and exit')
    args, remaining = parser.parse_known_args()
    if args.list_devices:
        print(sd.query_devices())
        parser.exit(0)
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[parser])
    parser.add_argument(
        'filename', nargs='?', metavar='FILENAME',
        help='audio file to store recording to')
    parser.add_argument(
        '-d', '--device', type=int_or_str,
        help='input device (numeric ID or substring)')
    parser.add_argument(
        '-r', '--samplerate', type=int, help='sampling rate')
    parser.add_argument(
        '-c', '--channels', type=int, default=1, help='number of input channels')
    parser.add_argument(
        '-t', '--subtype', type=str, help='sound file subtype (e.g. "PCM_24")')
    args = parser.parse_args(remaining)

    q = queue.Queue()

    def callback(indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        q.put(indata.copy())

    try:
        if args.samplerate is None:
            device_info = sd.query_devices(args.device, 'input')
            # soundfile expects an int, sounddevice provides a float:
            args.samplerate = int(device_info['default_samplerate'])

        args.filename = soundpath

        # Make sure the file is opened before recording anything:
        with sf.SoundFile(args.filename, mode='x', samplerate=args.samplerate,
                          channels=args.channels, subtype=args.subtype) as file:
            with sd.InputStream(samplerate=args.samplerate, device=args.device,
                                channels=args.channels, callback=callback):
                print('#' * 80)
                print('press Ctrl+C to stop the recording')
                print('#' * 80)

                while True:

                    file.write(q.get())
                    # focus on here since it's where keyboard entered
                    if keyboard.is_pressed("r"):
                        raise KeyboardInterrupt

    except KeyboardInterrupt:
        print('\nRecording finished: ' + repr(args.filename))

        speech = convertSpeech(soundpath)
        translate(speech)
        parser.exit(0)
    except Exception as e:
        parser.exit(type(e).__name__ + ': ' + str(e))


def convertSpeech(soundpath):
    r = sr.Recognizer()
    with sr.AudioFile(soundpath) as source:
        audio_text = r.listen(source)

    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        # using google speech recognition
        text = r.recognize_google(audio_text)
        print('Converting audio transcripts into text ...')
        # print(text)
        sys.stdout.write(text)
        return text
    except:
        print('Sorry.. run again...')


# Start the program without app if run by "other" way
if __name__ == '__main__':
    soundpath = 'output.wav'
    # press r to stop the recording
    record_asynch(soundpath)
