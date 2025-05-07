from kivy.core.audio import SoundLoader

slider_move = 0
button_down = 1
button_up = 2
engine = 3
data_reveal = 4
computer_processing = 5


def play_sound(sound_type):
    if sound_type is slider_move:
        sound = SoundLoader.load('sounds/slider_move.wav')
        sound.volume = 0.1
    elif sound_type is button_down:
        sound = SoundLoader.load('sounds/button_down.wav')
        sound.volume = 0.1
    elif sound_type is button_up:
        sound = SoundLoader.load('sounds/button_up.wav')
        sound.volume = 0.1
    elif sound_type is computer_processing:
        sound = SoundLoader.load('sounds/computer_processing.wav')
        sound.volume = 0.1
    elif sound_type is data_reveal:
        sound = SoundLoader.load('sounds/data_reveal.wav')
        sound.volume = 0.1
    else:
        sound = SoundLoader.load('sounds/engine.wav')
        sound.volume = 0.3
    if sound:
        sound.play()
