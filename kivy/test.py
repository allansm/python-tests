from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.config import Config

Config.set('graphics', 'width', '140')
Config.set('graphics', 'height', '45')
Config.set('graphics', 'resizable', False)

Builder.load_file('button.kv')

class root(Widget):
    def event(self):
        print("helloworld from kivy")

class app(App):
    def build(self):
        return root()
    
app().run()
