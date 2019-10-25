from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.behaviors import ButtonBehavior,ToggleButtonBehavior
from kivy.uix.image import Image
from kivy.properties import StringProperty,NumericProperty,ListProperty
from kivy.uix.floatlayout import FloatLayout
Builder.load_string('''

<Navbar>:
    size_hint:1,None
    height:"30sp"
    BtnImg:
        color:root.btn_menu_color
        source:"asset/3btn.png"    
        size_hint:None,1
        width:"30sp"
        on_press:
            self.color=0,1,1,.5
            root.on_press_menu()
        on_release:
            self.color=root.btn_menu_color
            root.on_release_menu()
    Label
        text:root.app_name
        font_size:self.height/1.5
        halign:"right"
        valign:"middle"
        text_size:self.size
        color:root.app_name_color
    Label:
        size_hint:None,1
        width:"10sp"
    BtnImg:
        id:qrbtn
        color:root.btn_menu_color
        source:"asset/qr.png"    
        size_hint:None,1
        width:"20sp"
        on_press:
            self.color=0,1,1,.5
            root.scanbtn+=1
        on_release:
            self.color=root.btn_menu_color
            
        
''')
class BtnImg(ButtonBehavior,Image):

    pass
class NavBar(BoxLayout):
    scanbtn=NumericProperty(0)
    menu_pressed=StringProperty("normal")
    menu_released=StringProperty("down")
    app_name = StringProperty("My Aplication")
    btn_menu_color=ListProperty([1,1,1,1])
    app_name_color=ListProperty([1,1,1,1])

    def __init__(self, *args, **kwargs):
        super(NavBar, self).__init__(*args, **kwargs)
    def on_press_menu(self):
        self.menu_pressed="down"
        self.menu_released="normal"
    def on_release_menu(self):
        self.menu_released="down"
        self.menu_pressed = "normal"
    def press(self,a,b):
        print(a,b)
    def on_scanbtn(self,a,b):
        pass

