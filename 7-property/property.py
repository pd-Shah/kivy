from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.anchorlayout import AnchorLayout


class MyApp(App):
    pass


class Mywidget(AnchorLayout):
    label_text= ObjectProperty()
    my_button= ObjectProperty()
    def Print(self):
        self.label_text.text="change text"
        self.my_button.text="changed!"


if __name__=="__main__":
    MyApp().run()
