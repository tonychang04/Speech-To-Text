import kivy
from kivy.app import App
from kivy.uix.label import Label

class SpeechApp(App):
    def build(self):
        return Label(text="tech with tim")