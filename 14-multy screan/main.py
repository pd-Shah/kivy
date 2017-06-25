
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

class MenuScreen(Screen):
    pass

class NewGameScreen(Screen):
    class XY(Widget):
        def on_touch_down(self, touch):
            with self.canvas:
                sm.current="load"


class LoadGameScreen(Screen):
    class YX(Widget):
        def on_touch_down(self, touch):
            with self.canvas:
                sm.current="menu"

buildKV = Builder.load_file("hue.kv")
sm=ScreenManager()
sm.add_widget(MenuScreen(name="menu"))
sm.add_widget(LoadGameScreen(name="load"))

class HueApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    HueApp().run()

