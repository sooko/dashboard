from dial import DialPressure,DialTacho,DialSpeed
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.clock import Clock
# from android.permissions import request_permission, Permission
# request_permission(Permission.CAMERA)
from kivy.uix.behaviors import ButtonBehavior,ToggleButtonBehavior
from kivy.uix.image import Image
import binascii
# from chart import Chart
from kivy.properties import ObjectProperty
from kivy.garden.navigationdrawer import NavigationDrawer
from kivy.uix.button import Button
from math import sin
from kivy.garden.graph import Graph, MeshLinePlot,LinePlot
from kivy.uix.floatlayout import FloatLayout
from navbar import NavBar
from pressure import PressurePage
from kivy.properties import StringProperty,NumericProperty,BooleanProperty,ListProperty
from able import BluetoothDispatcher,GATT_SUCCESS,Advertisement
from throttle import ThrottlePage
from error_message import install_exception_handler
from pressure import PressurePage
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
    
    anim_type:"slide_above_anim"
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
        canvas:
            Color:
                rgba:1,1,1,.2
            Rectangle:
                size:self.size
                pos:self.pos
                source:"asset/ungu.png"
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
                    Label:
                        height:"30sp"
                        size_hint:1,None
                    BtnImage
                        text:"pressure gauge"
                        on_press:
                            root.app_name="pressure_gauge"
                            root_page.clear_widgets()
                            root.ble.stop_scan()
                            root_page.add_widget(PressurePage())
                            root.ble.start_scan()
                            root.dev="pressure"
                        on_release:
                            root.toggle_state(False)
                    BtnImage
                        text:"Throttle Balance"
                        on_press:
                            root.app_name="Throttle Balance"
                            root_page.clear_widgets()
                            root_page.add_widget(ThrottlePage())
                            root.dev="throttle"
                        on_release:
                            root.toggle_state(False)
    FloatLayout:
        canvas:
            Color:
                rgba:1,1,1,.2
            Rectangle:
                size:self.size
                pos:self.pos
                source:"asset/ungu.png"
        BoxLayout:
            canvas:
                Color:
                    rgba:1,1,1,.1
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    source:"asset/ungu.png"
            size_hint:.9,.95
            pos_hint:{"center_x":.5,"center_y":.5}
            orientation:"vertical"
            NavBar:
                app_name:root.app_name
                btn_menu_color:0,1,1,1
                app_name_color:0,1,1,1
                on_menu_pressed:root.toggle_state()
                on_scanbtn:root.open_qrscan()
            FloatLayout:
                id:root_page
                pos_hint:{"center_x":.5,"center_y":.5}
                
                
        BoxLayout:
            orientation:"vertical"
            Label:
                text:"{}".format(root.data_adv)
            Label:
                text:root.data_batt           
            Label:
                text:root.data_pressure  
        FloatLayout:
            id:qr
            pos_hint:{"center_x":.5,"center_y":.5}
            size_hint:.7,.5  
            orientation: 'vertical'
''')
class BtnImage(Button):
    pass
class MainLayout(NavigationDrawer):
    ble = BluetoothDispatcher()
    app_name=StringProperty("")
    data_adv=StringProperty("")
    data_pressure=StringProperty("")
    data_batt=StringProperty("")
    dev=StringProperty("pressure")
    pressure_id=StringProperty("")
    throttle_id=StringProperty("")
    def __init__(self,*args,**kwargs):
        super(MainLayout,self).__init__(*args,**kwargs)
        self.ids["root_page"].add_widget(PressurePage())
        self.ble.bind(on_device=self.on_device)
        try:
            self.ble.start_scan()
        except:
            pass
    def on_device(self, ble, device, rssi, advertisement):
        for ad in advertisement:
            if ad.ad_type == Advertisement.ad_types.manufacturer_specific_data:
                self.data_adv=str(binascii.hexlify(ad.data).decode())
                self.data_pressure = str(int(self.data_adv[12:16], 16) / 1.2593856/2)
                if self.dev=="pressure":
                    try:
                        self.give_pressure_data(int(self.data_adv[12:16], 16) / 1.2593856/2-1.588,int(self.data_adv[8:12], 16)/51.33)
                    except:
                        pass
                if self.dev=="throttle":
                    try:
                        self.give_throttle_data(int(self.data_adv[8:12], 16),
                                                int(self.data_adv[12:16], 16),
                                                int(self.data_adv[16:20], 16),
                                                int(self.data_adv[20:24], 16),
                                                int(self.data_adv[24:28], 16))
                    except:
                        pass
    def open_qrscan(self):
        print("yaaaa")
    def give_pressure_data(self,data,data_volt):
        self.ids["root_page"].children[0].show_value(data,data_volt)
    def give_throttle_data(self,batt,cyl1,cyl2,cyl3,cyl4):
        self.ids["root_page"].children[0].show_value(batt,cyl1,cyl2,cyl3,cyl4)
class DashBoard(App):
    ml=MainLayout()
    def build(self):
        return self.ml
    def on_pause(self):
        self.ml.ble.stop_scan()
        return True
    def on_resume(self):
        self.ml.ble.start_scan()
        pass
    def on_stop(self):
        self.ml.ble.stop_scan()
if __name__=="__main__":
    DashBoard().run()