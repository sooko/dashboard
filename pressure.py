from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from able import BluetoothDispatcher,GATT_SUCCESS,Advertisement
from dial import DialPressure
from kivy.properties import StringProperty,NumericProperty
from chart import Chart
from kivy.clock import Clock
import binascii
from kivy.app import App
Builder.load_string('''
<PressurePage>:
    pos_hint:{"center_x":.5,"center_y":.5}
    spacing:1
    orientation:"vertical"
    FloatLayout:
        size_hint:1,1
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
        size_hint:1,.7
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

class PressurePage(BoxLayout):
    ble=BluetoothDispatcher()
    data_adv=StringProperty("")
    data_pressure=StringProperty("")
    clock=Clock
    count=NumericProperty(0)
    state=NumericProperty(0)
    def __init__(self,*args,**kwargs):
        super(PressurePage,self).__init__(**kwargs)
        self.ids['chart'].plot_pressure.points.clear()
        print("clear")
        self.ble.bind(on_device=self.on_device)
        self.ble.stop_scan()
        self.ble.start_scan()
        self.clock.schedule_interval(self.cb,.1)
    def cb(self,dt):
        if self.state==1:
            self.count+=1
            self.ids["chart"].show_chart_pressure(self.count,self.ids["psi"].value)
    def on_device(self, ble, device, rssi, advertisement):
        for ad in advertisement:
            if ad.ad_type == Advertisement.ad_types.manufacturer_specific_data:
                self.data_adv=str(binascii.hexlify(ad.data).decode())
                self.data_pressure=str(int(self.data_adv[12:16],16)/1.2593856/6.8947503)
                self.ids["psi"].show_value(int(self.data_adv[12:16],16)/1.2593856/6.8947503)
                self.state=1
