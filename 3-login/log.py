from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return MyWidget()

class MyWidget(GridLayout):

    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)

        self.cols=2

        self.user_name=TextInput(multiline=False)
        self.add_widget(Label(text="user name"))
        self.add_widget(self.user_name)

        self.password=TextInput(multiline=False, password=True)
        self.add_widget(Label(text="password"))
        self.add_widget(self.password)



if __name__=="__main__":
    MyApp().run()

