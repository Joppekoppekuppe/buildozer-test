import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
kv = '''
<MyRoot>:
    BoxLayout:
        orientation: "vertical"
        Button:
            text: "lukitse"
            font_size: 32
            on_press: root.lukitse()
        Button:
            text: "avaa lukitus"
            font_size: 32
            on_press: root.avaa()

'''
class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot, self).__init__()
    def lukitse(self):
       pass
    def avaa(self):
        pass
class Ruutuaika(App):
    def build(self):
        return MyRoot()
ruutuaika = Ruutuaika()
ruutuaika.run()