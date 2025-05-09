from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen



class GameScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(orientation='horizontal', spacing=10, padding=10)

        # Column left – Player list
        self.players_list = BoxLayout(orientation='vertical', spacing=5, size_hint_x = 1/10)
        self.players_list.add_widget(Label(text="Player 1"))
        self.players_list.add_widget(Label(text="Player 2"))
        self.players_list.add_widget(Label(text="Player 3"))
        self.players_list.add_widget(Label(text="Player 4"))
        self.players_list.add_widget(Label(text="Player 5"))
        self.players_list.add_widget(Label(text="Player 6"))
        self.players_list.add_widget(Label(text="Player 7"))
        self.players_list.add_widget(Label(text="Player 8"))
        root.add_widget(self.players_list)

        # Column middle – Boards and Hand
        self.boards_and_hand = BoxLayout(orientation='vertical', spacing=5, size_hint_x = 7/10)
        self.boards_and_hand.add_widget(Label(text='Bob or Enemy'))
        self.boards_and_hand.add_widget(Label(text="Enemy Board / Tavern"))
        self.boards_and_hand.add_widget(Label(text="My Board"))
        self.boards_and_hand.add_widget(Label(text="My Hand"))
        self.boards_and_hand.add_widget(Label(text='My Hero'))
        root.add_widget(self.boards_and_hand)

        # Column right – Misc Info and Back Button
        self.info_panel = BoxLayout(orientation='vertical', spacing=5, size_hint_x= 2/10)
        self.info_panel.add_widget(Label(text="Enemy Buffs"))
        self.info_panel.add_widget(Label(text="Global Effects"))
        self.info_panel.add_widget(Label(text="My Buffs"))

        back_btn = Button(text="Back to Settings", size_hint_y=None, height=40)
        back_btn.bind(on_release=self.back_to_settings)
        self.info_panel.add_widget(back_btn)

        root.add_widget(self.info_panel)

        self.add_widget(root)

    def back_to_settings(self, instance):
        self.manager.current = 'settings'
