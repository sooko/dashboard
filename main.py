from dial import DialPressure,DialTacho,DialSpeed
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.clock import Clock
import binascii
from chart import Chart
from kivy.properties import ObjectProperty
from kivy.garden.navigationdrawer import NavigationDrawer
from math import sin
from kivy.garden.graph import Graph, MeshLinePlot,LinePlot
# from able import GATT_SUCCESS, Advertisement, BluetoothDispatcher
from kivy.uix.floatlayout import FloatLayout
from navbar import NavBar
from able import BluetoothDispatcher, GATT_SUCCESS,Advertisement
from kivy.properties import StringProperty,NumericProperty,BooleanProperty,ListProperty
Builder.load_string('''
#:import MeshLinePlot kivy.garden.graph.MeshLinePlot
<MainLayout>:
    canvas:
        Color:
            rgba:1,1,1,.71
        BorderImage:
            border:0,0,0,0
            size:self.size
            pos:self.pos
            source:"asset/frame.png"
    id:nd
    BoxLayout:
    FloatLayout:
        BoxLayout:
            size_hint:.9,.95
            pos_hint:{"center_x":.5,"center_y":.5}
            orientation:"vertical"
            ScreenManager:
                Screen
                    name:"psi"
                    BoxLayout:
                        spacing:1
                        orientation:"vertical"
                        NavBar:
                            app_name:"pressure gauge  "
                            btn_menu_color:0,1,1,1
                            app_name_color:0,1,1,1
                            on_menu_pressed:root.toggle_state()
                            
                            
                        FloatLayout:
                            size_hint:1,None
                            height:"350sp"
                            pos_hint:{"center_x":.5,"center_y":.5}
                            DialPressure:
                                pos_hint:{"center_x":.5,"center_y":.5}
                                id:psi
                        BoxLayout:
                            size_hint:1,None
                            pos_hint:{"right":1}
                            height:"60sp"
                            orientation:"vertical"
                            padding:5
                            canvas.before:
                                Color:
                                    rgba:0,1,1,.4
                                RoundedRectangle:
                                    size:self.size
                                    pos:self.pos
                                    source:"asset/gradient_blue.png"
                            Label:
                                text:"  Battery"
                                color:0,1,1,1
                                font_size:self.height
                                halign:"left"
                                valign:"middle"
                                text_size:self.size
                                size_hint:1,.9
                            Label:
                                text:"    12v"
                                markup:True
                                color:0,1,1,1
                                font_size:self.height
                                halign:"left"
                                valign:"middle"
                                text_size:self.size
                        Label:
                            size_hint:1,None
                            height:"5sp"
                        FloatLayout:
                            id:flt
                            size_hint:1,1
                            pos_hint:{"center_x":.5,"center_y":.5}
                            Chart:
                                pos_hint:{"center_x":.5,"center_y":.5}
                                id:chart
                        BoxLayout:
                            size_hint:1,None
                            height:"20sp"
                            Label:
                                text:"pressure"
                                color:1,0,0,1
                            Label:
                                text:"battery"
                                color:1,1,0,1
                        
                            
                        

''')
class MainLayout(NavigationDrawer):
    data_adv=StringProperty("")
    def __init__(self,*args,**kwargs):
        super(MainLayout,self).__init__(*args,**kwargs)
        self.ids["chart"].show_chart(10,10)


class DashBoard(App):
    ml=MainLayout()
    def build(self):
        return self.ml
if __name__=="__main__":
    DashBoard().run()