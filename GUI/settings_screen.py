from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.uix.slider import Slider

from GUI.play_sound import play_sound, Sound


class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        layout.add_widget(Label(text="Welcome to Hearthstone Battlegrounds Clone", size_hint_y=3 / 10, font_size=42))
        layout.add_widget(Label(text="Settings Window", size_hint_y=2 / 10, font_size=30))
        screen_shake_setting = BoxLayout(orientation='horizontal', size_hint_y=3 / 10)
        layout.add_widget(screen_shake_setting)
        screen_shake_label_key = Label(text='screen shake', font_size=24, size_hint_x=1 / 5)
        self.screen_shake_slider = Slider(min=0, max=5, value=1, step=1, size_hint_x=3 / 5)
        self.screen_shake_slider.bind(value=self.screen_shake_slider_on_value)
        self.screen_shake_label_value = Label(text='1', font_size=30, size_hint_x=1 / 5)
        screen_shake_setting.add_widget(screen_shake_label_key)
        screen_shake_setting.add_widget(self.screen_shake_slider)
        screen_shake_setting.add_widget(self.screen_shake_label_value)
        start_btn = Button(text="Start Game", size_hint_y=2 / 10)
        start_btn.bind(on_release=self.start_game)
        layout.add_widget(start_btn)

        self.add_widget(layout)

    def start_game(self, instance):
        play_sound(Sound.button_down)
        self.manager.current = 'game'
        play_sound(Sound.button_up)

    def screen_shake_slider_on_value(self, instance, value):
        play_sound(Sound.slider_move)
        self.screen_shake_label_value.text = str(int(value))
