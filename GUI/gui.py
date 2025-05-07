from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        layout.add_widget(Label(text="Settings", font_size=32))
        start_button = Button(text="Start Game", size_hint=(1, 0.2))
        start_button.bind(on_press=self.start_game)
        layout.add_widget(start_button)

        self.add_widget(layout)

    def start_game(self, instance):
        self.manager.current = 'game'


class GameScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        main_layout = BoxLayout(orientation='horizontal', padding=10, spacing=10)

        # Left column: List of players
        left_col = BoxLayout(orientation='vertical', size_hint=(0.2, 1))
        left_col.add_widget(Label(text="Player 1"))
        left_col.add_widget(Label(text="Player 2"))
        left_col.add_widget(Label(text="Player 3"))
        left_col.add_widget(Label(text="..."))

        # Middle column: Boards and hand
        mid_col = BoxLayout(orientation='vertical', spacing=10, size_hint=(0.6, 1))
        mid_col.add_widget(Label(text="Enemy Board / Tavern", size_hint=(1, 0.3)))
        mid_col.add_widget(Label(text="My Board", size_hint=(1, 0.3)))
        mid_col.add_widget(Label(text="My Hand", size_hint=(1, 0.3)))

        # Right column: Game info and settings
        right_col = BoxLayout(orientation='vertical', spacing=10, size_hint=(0.2, 1))
        right_col.add_widget(Label(text="Enemy Buffs/HP/Armor"))
        right_col.add_widget(Label(text="Global Effects / Anomalies"))
        right_col.add_widget(Label(text="My Buffs/HP/Armor"))

        settings_btn = Button(text="Back to Settings", size_hint=(1, 0.2))
        settings_btn.bind(on_press=self.back_to_settings)
        right_col.add_widget(settings_btn)

        # Add all columns to main layout
        main_layout.add_widget(left_col)
        main_layout.add_widget(mid_col)
        main_layout.add_widget(right_col)

        self.add_widget(main_layout)

    def back_to_settings(self, instance):
        self.manager.current = 'settings'


class HearthstoneApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(GameScreen(name='game'))
        return sm

