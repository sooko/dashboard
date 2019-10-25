from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
Builder.load_string('''
<Home>:
    cols:2
    Button
    Button
    Button
    Button
    





''')

class Home(GridLayout):
    pass