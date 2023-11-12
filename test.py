import kivy
from kivy.app import App
from kivy.uix.label import Label
class Test(App):
    def build(self):
        return Label(text='hei')
test = Test()
test.run()
