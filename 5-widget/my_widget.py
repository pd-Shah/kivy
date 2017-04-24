
'''Widgets
Kivy uses the word widget to describe any user interface element. Just a few examples
of widgets include:
    The label you rendered in Example 1-3
    The text input field and buttons youll render shortly
    Layout classes that comprise other widgets and determine where they should be displayed
    Complicated tree views such as file pickers
    Movie and photo renderers
    Tabbed boxes that display different widgets depending on the selected tab
'''

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class widgetsApp(App):
    pass

class MyForm(BoxLayout):
    pass

if __name__=="__main__":
    widgetsApp().run()
