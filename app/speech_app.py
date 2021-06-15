import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget

from app import app_grid
from app.app_grid import MyGrid


class SpeechApp(App):
    def build(self):
        return MyGrid()