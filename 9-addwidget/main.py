from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class EventApp(App):
    pass

class rootWidget(BoxLayout):
    def clear_widget(self):
        self.clear_widgets()

    def new_widget(self):
        from kivy.uix.label import Label
        self.clear_widgets()
        self.add_widget(Label(text="new View"))


class EventForm(BoxLayout):
    def Print(self):
        print("EventForm")

class ChangeForm(BoxLayout):
    def Print(self, text):
        print(text)


if __name__=="__main__":
    EventApp().run()
