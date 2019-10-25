from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from dial import DialPressure
from kivy.properties import StringProperty,NumericProperty
from chart import ChartPressure
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
            text:"    {:.1f}v".format(root.batt)
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
        ChartPressure:
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
    data_adv=StringProperty("")
    data_pressure=StringProperty("")
    clock=Clock
    count=NumericProperty(0)
    state=NumericProperty(0)
    val=NumericProperty(0)
    y_chart=NumericProperty(0)
    batt=NumericProperty(0)
    def __init__(self,*args,**kwargs):
        super(PressurePage,self).__init__(**kwargs)
        # self.ids['chart'].plot_pressure.points=[(0,0)]
        print("clear")
        self.clock.schedule_interval(self.cb,.2)
    def cb(self,dt):
        if self.state==1:
            self.count+=1
            self.ids["chart"].show_chart_pressure(self.count,self.y_chart)
    def show_value(self,data,data_volt):
        self.ids["psi"].show_value(data)
        self.y_chart=data
        self.state=1
        self.batt=data_volt
