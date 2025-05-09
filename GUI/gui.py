from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window

from GUI.game_window import GameScreen
from GUI.settings_screen import SettingsScreen



# Set window size (90% of screen size)
screen_width, screen_height = Window.system_size
window_width = int(screen_width * 0.9)
window_height = int(screen_height * 0.9)
Window.size = (window_width, window_height)

# Center the window *after* setting its size
Window.left = (screen_width - window_width) // 2
Window.top = (screen_height - window_height) // 2

class HearthstoneApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(GameScreen(name='game'))
        return sm

