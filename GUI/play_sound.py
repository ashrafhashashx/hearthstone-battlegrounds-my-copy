from enum import Enum

from kivy.core.audio import SoundLoader

class Sound(Enum):
    slider_move = 0
    button_down = 1
    button_up = 2
    engine = 3
    data_reveal = 4
    computer_processing = 5

SOUNDS_PATH = 'GUI/sounds/'

def play_sound(sound_type):
    if sound_type is Sound.slider_move:
        sound = SoundLoader.load(f'{SOUNDS_PATH}slider_move.wav')
        sound.volume = 0.1
    elif sound_type is Sound.button_down:
        sound = SoundLoader.load(f'{SOUNDS_PATH}button_down.wav')
        sound.volume = 0.1
    elif sound_type is Sound.button_up:
        sound = SoundLoader.load(f'{SOUNDS_PATH}button_up.wav')
        sound.volume = 0.1
    elif sound_type is Sound.computer_processing:
        sound = SoundLoader.load(f'{SOUNDS_PATH}computer_processing.wav')
        sound.volume = 0.1
    elif sound_type is Sound.data_reveal:
        sound = SoundLoader.load(f'{SOUNDS_PATH}data_reveal.wav')
        sound.volume = 0.1
    else:
        sound = SoundLoader.load(f'{SOUNDS_PATH}engine.wav')
        sound.volume = 0.3
    if sound:
        sound.play()
