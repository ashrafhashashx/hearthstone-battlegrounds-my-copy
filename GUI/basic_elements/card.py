from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image


class Card(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.image = Image()