import numpy as np
import speech_recognition as sr
import argparse
import queue
import sys
import keyboard
import sounddevice as sd
import soundfile as sf
import os

from googletrans import Translator
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from scipy.io.wavfile import write

import keyboard
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from functools import partial

class MyGrid(Widget):
    def button_record_translate(self):
        """
        Record and translate the given text.
        :return:
        """
        recorded_text, translated_text = record_translate('output.wav')
        if (recorded_text == None or translated_text == None):
            self.ids.text_label.text = 'Error in recording'
            return
        self.ids.text_label.text = 'Message: ' + recorded_text + '\n' + 'Translation: ' + translated_text


def translate(speech):
    """
    Translate the given speech
    :param speech: the string text being given
    :return: the returned string changed based on the language
    """
    translator = Translator()
    word = translator.translate(speech, dest='zh-cn')
    print(word.text)
    return word.text

def record_translate(soundpath):
    """
    Record the audio and save locally
    :param soundpath: the path you want to save to the file
    :return:
    """
    fs = 44100  # free-air resonant frequency
    seconds = 10  # Changed the prefixed time
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()  # wait until the recording is done
    processed_recording = (np.iinfo(np.int32).max *
                           (myrecording / np.abs(myrecording).max())).astype(np.int32)
    write(soundpath, fs, processed_recording)
    text = convertSpeech(soundpath)
    translated_text = translate(text)
    return text, translated_text


def convertSpeech(soundpath):
    """
    Convert the given speech to text.
    :param soundpath: the soundpath that the audio belongs to
    :return: the string of text based on the speech
    """
    r = sr.Recognizer()
    with sr.AudioFile(soundpath) as source:
        audio_text = r.listen(source)

    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        # using google speech recognition
        text = r.recognize_google(audio_text)
        print('Converting audio transcripts into text ...')
        #print(text)
        sys.stdout.write(text)
        return text
    except:
        print('Sorry.. run again...')
