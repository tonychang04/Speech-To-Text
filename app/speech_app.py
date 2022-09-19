from kivy.app import App

from .app_grid import MyGrid

class SpeechApp(App):
    def build(self):
        return MyGrid()