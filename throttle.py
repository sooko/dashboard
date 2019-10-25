from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.properties import StringProperty,NumericProperty,ListProperty
from kivy.garden.graph import Graph, MeshLinePlot,LinePlot
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.uix.behaviors import DragBehavior
from kivy.core.audio import SoundLoader
from kivy.uix.label import Label
from kivy.uix.image import Image
from chart import ChartThrottle
Builder.load_string('''
<DragLabel>:
    drag_rectangle: self.x, self.y, self.width, self.height
    drag_timeout: 10000000
    drag_distance: 0
<Labele@Label>:
    halign:"right"
    valign:"middle"
    text_size:self.size
<TabungMbok@FloatLayout>:
    pos_hint:{"center_x":.5,"center_y":.5}
    
    canvas:
        Color:
            rgba:1,1,1,.05
        Rectangle:
            size:self.size
            pos:self.pos
<Tabung@FloatLayout>:
    
    pos_hint:{"center_x":.5,"center_y":.5}
    canvas:
        Color:
            rgba:0,1,1,.3
        Rectangle:
            size:self.size
            pos:self.pos
            source:"asset/batang.png"

<Tabung1@Label>:
    value:120
    size_hint:.6,root.value/120
    pos_hint:{"center_x":.5,"y":0}
    canvas:
        Color:
            rgba:0,1,1,.3
        Rectangle:
            size:self.size
            pos:self.pos
            
<ThrottlePage>:
    pos_hint:{"center_x":.5,"center_y":.5}
    BoxLayout:
        pos_hint:{"center_x":.5,"center_y":.5}
        orientation:"vertical"
        Label: 
            size_hint:1,None
            height:"20sp"
        FloatLayout:
            id:ok
            pos_hint:{"center_x":.5,"center_y":.5}
            BoxLayout:
                padding:20,0,20,0
                
                spacing:10
                pos_hint:{"center_x":.5,"center_y":.5}
                TabungMbok
                    Tabung1  
                        value:root.cyl1_value
                    Tabung:
                TabungMbok
                    Tabung1  
                        value:root.cyl2_value
                    Tabung:
                TabungMbok
                    Tabung1  
                        value:root.cyl3_value
                    Tabung:
                TabungMbok
                    Tabung1  
                        value:root.cyl4_value
                    Tabung:
            ChartThrottle
                pos_hint:{"center_x":.5,"center_y":.494}
                id:chart
                ymax:120
                border_color:1,1,1,1
                y_ticks_minor:5
                xmax:9
                x_ticks_major:0
                x_grid_label:False
                y_grid_label:False
                x_grid_label:False
                x_grid:False
                y_grid:True
        BoxLayout:
            pos_hint:{"center_x":.5,"center_y":.5}
            size_hint:1,.05
            padding:20,0,20,0
            spacing:10
            Label:
                color:0,1,1,1
                text:"{:.1f}".format(root.cyl1_value)
                font_size:self.height/1.5
            Label:
                color:0,1,1,1
                font_size:self.height/1.5
                text:"{:.1f}".format(root.cyl2_value)
            Label:
                color:0,1,1,1
                font_size:self.height/1.5
                text:"{:.1f}".format(root.cyl3_value)
            Label:
                color:0,1,1,1
                font_size:self.height/1.5
                text:"{:.1f}".format(root.cyl4_value)
        BoxLayout:
            pos_hint:{"center_x":.5,"center_y":.5}
            size_hint:1,.05
            padding:20,0,20,0
            spacing:10
            Label:
                text:"Kpa"
                halign:"center"
                valign:"top"
                text_size:self.size
                font_size:self.height/2
                color:0,1,1,1
            Label:
                color:0,1,1,1
                text:"Kpa"
                halign:"center"
                valign:"top"
                text_size:self.size
                font_size:self.height/2
            Label:
                color:0,1,1,1
                text:"Kpa"
                halign:"center"
                valign:"top"
                font_size:self.height/2
                text_size:self.size
            Label:
                color:0,1,1,1
                text:"Kpa"
                halign:"center"
                valign:"top"
                text_size:self.size
                font_size:self.height/2
    
''')
class DragLabel(DragBehavior, Image):
    pass


class ThrottlePage(FloatLayout):
    cyl1_value=NumericProperty(120)
    cyl2_value=NumericProperty(120)
    cyl3_value=NumericProperty(120)
    cyl4_value=NumericProperty(120)
    state=NumericProperty(0)
    clock=Clock
    batt=NumericProperty(0)
    def __init__(self,*args,**kwargs):
        super(ThrottlePage,self).__init__(**kwargs)
        self.demo()
    def demo(self):
        self.anim1 = Animation(cyl1_value=0, duration=1.5,t="out_bounce")
        self.anim2 = Animation(cyl2_value=0, duration=1.5,t="out_bounce")
        self.anim3 = Animation(cyl3_value=0, duration=1.5,t="out_bounce")
        self.anim4 = Animation(cyl4_value=0, duration=1.5,t="out_bounce")
        self.anim1.start(self)
        self.anim2.start(self)
        self.anim3.start(self)
        self.anim4.start(self)
        self.clock.schedule_once(self.delay,3)
    def delay(self,dt):
        self.state=1
    def show_value(self,batt,cyl1,cyl2,cyl3,cyl4):
        if self.state==1:
            self.batt=batt
            self.cyl1_value=cyl1
            self.cyl2_value=cyl2
            self.cyl3_value=cyl3
            self.cyl4_value=cyl4















