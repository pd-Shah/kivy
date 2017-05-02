from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

class MainMenu(BoxLayout):

    def enter_sentences_button(self):
        self.clear_widgets()
        self.add_widget(EnterSentences())

    def review_button(self):
        self.clear_widgets()
        self.add_widget(Review())


class EnterSentences(BoxLayout):
    search_box = ObjectProperty()
    def main_menu(self):
        self.clear_widgets()
        self.add_widget(MainMenu())


class Review(BoxLayout):
    pass

class NewApp(App):
    pass


if __name__ == "__main__":
    NewApp().run()
