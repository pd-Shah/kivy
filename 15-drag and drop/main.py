from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.behaviors import DragBehavior
from kivy.lang import Builder
from kivy.uix.button import Button
# You could also put the following in your kv file...
kv = '''
<DragLabel>:
    # Define the properties for the DragLabel
    drag_rectangle: self.x, self.y, self.width, self.height
    drag_timeout: 10000000
    drag_distance: 0

FloatLayout:
    # Define the root widget
    DragLabel:
        size_hint: 0.25, 0.2
        text: 'Drag me'
'''


class DragLabel(DragBehavior, Button):
    pass


class TestApp(App):
    def build(self):
        return Builder.load_string(kv)

TestApp().run()


from kivy.app import App
from kivy.core.window import Window


class WindowFileDropExampleApp(App):
    def build(self):
        Window.bind(on_dropfile=self._on_file_drop)
        return

    def _on_file_drop(self, window, file_path):
        print(file_path)
        return

if __name__ == '__main__':
    WindowFileDropExampleApp().run()

