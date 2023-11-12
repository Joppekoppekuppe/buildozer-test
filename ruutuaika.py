import kivy
from kivy.app import App
from kivy.uix.label import Label
class Ruutuaika(App):
    def build(self):
        return Label(text='hei')
ruutuaika = Ruutuaika()
ruutuaika.run()
