from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class EventApp(App):
    pass

class rootWidget(BoxLayout):
    def clear_widget(self):
        self.clear_widgets()




class Form1(BoxLayout):
    def goto_form2(self):
        from kivy.factory import Factory
        form2=Factory.Form2()
        self.clear_widgets()
        self.add_widget(form2)

class Form2(BoxLayout):
    def goto_form1(self):
        from kivy.uix.label import Label
        from kivy.factory import Factory
        self.clear_widgets()
        form1=Factory.Form1()
        self.add_widget(form1)



if __name__=="__main__":
    EventApp().run()
