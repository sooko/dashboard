from dial import DialPressure,DialTacho,DialSpeed
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.behaviors import ButtonBehavior,ToggleButtonBehavior
from kivy.uix.image import Image
import binascii
from chart import Chart
from kivy.properties import ObjectProperty
from kivy.garden.navigationdrawer import NavigationDrawer
from kivy.uix.button import Button
from math import sin
from kivy.garden.graph import Graph, MeshLinePlot,LinePlot
from kivy.uix.floatlayout import FloatLayout
from navbar import NavBar
from pressure import PressurePage
# from able import BluetoothDispatcher, GATT_SUCCESS,Advertisement
from kivy.properties import StringProperty,NumericProperty,BooleanProperty,ListProperty
Builder.load_string('''

#import MeshLinePlot kivy.garden.graph.MeshLinePlot
#:import PressurePage pressure.PressurePage
#:import ThrottlePage throttle.ThrottlePage

<BtnImage>:
    alpa:1
    text:""
    height:"60sp"
    size_hint:1,None
    background_normal:"asset/set.png"
    background_down:"asset/set_bg.png"
    color:0,1,1,1
<MainLayout>:
    anim_type:"slide_above_simple"
    canvas:
        Color:
            rgba:1,1,1,.71
        BorderImage:
            border:0,0,0,0
            size:self.size
            pos:self.pos
            source:"asset/frame.png"
    id:nd
    FloatLayout
        size_hint:1,.95
        pos_hint:{"center_x":.5,"center_y":.5}
        AnchorLayout:
            pos_hint:{"center_x":.5,"center_y":.5}
            anchor_x:"right"
            anchor_y:"center"
            ScrollView:
                size_hint:.95,1
                BoxLayout:
                    spacing:5
                    orientation:"vertical"
                    size_hint:1,None
                    height:self.minimum_height
                    BtnImage
                        text:"home"
                        on_press:
                    BtnImage
                        text:"pressure gauge"
                        on_press:
                            root.app_name="pressure_gauge"
                            root_page.clear_widgets()
                            root_page.add_widget(PressurePage())
                        on_release:
                            root.toggle_state(False)
                    BtnImage
                        text:"Throttle Balance"
                        on_press:
                            root.app_name="Throttle Balance"
                            root_page.clear_widgets()
                            root_page.add_widget(ThrottlePage())
                        on_release:
                            root.toggle_state(False)

                    BtnImage
                        text:"Fi Tacho"
                    BtnImage
                        text:"Battery Tester"
    FloatLayout:
        BoxLayout:
            size_hint:.9,.95
            pos_hint:{"center_x":.5,"center_y":.5}
            orientation:"vertical"
            NavBar:
                app_name:root.app_name
                btn_menu_color:0,1,1,1
                app_name_color:0,1,1,1
                on_menu_pressed:root.toggle_state()
            FloatLayout:
                id:root_page
                pos_hint:{"center_x":.5,"center_y":.5}
        BoxLayout:
            orientation:"vertical"
            Label:
                text:root.data_adv     
            Label:
                text:root.data_batt           
            Label:
                text:root.data_pressure               
''')
class BtnImage(Button):
    pass
class MainLayout(NavigationDrawer):
    app_name=StringProperty("")
    data_adv=StringProperty("")
    data_pressure=StringProperty("")
    data_batt=StringProperty("")
    current=StringProperty("home")
    # ble=BluetoothDispatcher()
    def __init__(self,*args,**kwargs):
        super(MainLayout,self).__init__(*args,**kwargs)
        # self.ble.bind(on_device=self.on_device)
        # self.ble.start_scan()
    def on_device(self, ble, device, rssi, advertisement):
        for ad in advertisement:
            if ad.ad_type == Advertisement.ad_types.manufacturer_specific_data:
                self.data_adv=str(binascii.hexlify(ad.data).decode())
                self.data_batt=str(int(self.data_adv[8:12],16))
                self.data_pressure=str(int(self.data_adv[12:16],16)/1.2593856)

class DashBoard(App):
    ml=MainLayout()
    def build(self):
        return self.ml



if __name__=="__main__":
    DashBoard().run()