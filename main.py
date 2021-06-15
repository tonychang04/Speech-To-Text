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
from scipy.io.wavfile import write

from app.speech_app import SpeechApp


# main methodr
if __name__ == '__main__':
    speechApp = SpeechApp()
    speechApp.run()
    #soundpath = 'output.wav'
    #translator = Translator()
    #print(translator)
    #record_asynch(soundpath)
    #output = translator.translate("is this translation accurate?", dest= "ko")
    #print(output.text, output.extra_data)
    #print(translator.translate("roses", dest='zh-cn'))
    #print(translation)
    #record(soundpath)
    
    print("wewe")
