from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Test(BoxLayout):
    pass

class HueApp(App):
    def build(self):
        return Test()

if __name__ == '__main__':
    HueApp().run()
