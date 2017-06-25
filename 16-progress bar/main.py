from kivy.app import App
from kivy.uix.popup import Popup
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.clock import Clock

import time, threading

class PopupBox(Popup):
    pop_up_text = ObjectProperty()
    def update_pop_up_text(self, p_message):
        self.pop_up_text.text = p_message

class ExampleApp(App):
    def show_popup(self):
        self.pop_up = Factory.PopupBox()
        self.pop_up.update_pop_up_text('Running some task...')
        self.pop_up.open()

    def process_button_click(self):
        # Open the pop up
        self.show_popup()

        # Call some method that may take a while to run.
        # I'm using a thread to simulate this
        mythread = threading.Thread(target=self.something_that_takes_5_seconds_to_run)
        mythread.start()

    def something_that_takes_5_seconds_to_run(self):
        thistime = time.time()
        while thistime + 5 > time.time(): # 5 seconds
            time.sleep(1)

        # Once the long running task is done, close the pop up.
        self.pop_up.dismiss()

if __name__ == "__main__":
    ExampleApp().run()

