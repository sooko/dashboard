from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.properties import NumericProperty,StringProperty,ListProperty
from kivy.app import App
from kivy.animation import Animation
from kivy.config import Config
from kivy.garden.graph import Graph, MeshLinePlot,LinePlot
from kivy.uix.screenmanager import ScreenManager,Screen
Config.set('graphics', 'height', 770)
Config.set('graphics', 'width', 370)
from kivy.clock import Clock
Builder.load_string("""
<Label>:
    font_name:"fonts/hemi.ttf"
<DialTacho>:
    Image:
        pos_hint: {"center_x":0.5, "center_y":0.5}
        source:"asset/rpm.png"
        size_hint:1,1
        color:root.warna
    FloatLayout:
        size_hint: None, None
        pos_hint: {"center_x":0.5, "center_y":0.5}
        size: .95*min(root.size), .95*min(root.size)
        canvas:
            Color:
                rgba: root.warna_alpa
            Ellipse:
                size: self.size     
                pos: self.pos
                source:"asset/green_bolong_bg.png"
                angle_start:219
                angle_end:220+root.anime_value/50
        BoxLayout:
            orientation:"vertical"
            size_hint:1,.5
            pos_hint:{"center_x":.5,"center_y":.5}
            Label:
                text:"rpm"
                font_size:self.height/1
                color:root.warna_name
            Label:
                text:str(root.value)
                font_size:self.height*1.15
                color:root.warna_value
            Label:
    FloatLayout:
        size_hint: None, None
        pos_hint: {"center_x":0.5, "center_y":0.5}
        size: .94*min(root.size), .94*min(root.size)
        canvas:
            Color:
                rgba: root.warna_alpa
            Ellipse:
                size: self.size     
                pos: self.pos
                source:"asset/green_bolong.png"
                angle_start:219
                angle_end:220+280
    Image:
        pos_hint:{"center_x":.5,"center_y":.5}
        source:"asset/pucuk.png"
        size_hint:1.15,1.15
        color:1,0,0,1
        canvas.before:
            PushMatrix
            Rotate:
                angle: 320-root.anime_max_value/50
                origin: self.center
        canvas.after:
            PopMatrix
    FloatLayout:
        size_hint: None, None
        pos_hint: {"center_x":0.5, "center_y":0.5}
        size: .94*min(root.size), .94*min(root.size)
        canvas:
            Color:
                rgba: 1,1,1,.1
            Ellipse:
                size: self.size     
                pos: self.pos
                source:"asset/moon.png"
                angle_start:219
                angle_end:220+root.anime_value/50
    Image:
        color:1,1,1,.85
        source:"asset/jarum_putih.png"
        size_hint:.7,.7
        pos_hint: {"center_x":0.5, "center_y":0.5}
        canvas.before:
            PushMatrix
            Rotate:
                angle: 140-root.anime_value/50
                origin: self.center
        canvas.after:
            PopMatrix
   
<DialPressure>:
    Image:
        pos_hint: {"center_x":0.5, "center_y":0.5}
        source:"asset/psi.png"
        size_hint:1,1
        color:root.warna
    FloatLayout:
        size_hint: None, None
        pos_hint: {"center_x":0.5, "center_y":0.5}
        size: .95*min(root.size), .95*min(root.size)
        canvas:
            Color:
                rgba: root.warna_alpa
            Ellipse:
                size: self.size     
                pos: self.pos
                source:"asset/green_bolong_bg.png"
                angle_start:219
                angle_end:220+root.anime_value*280/80
        BoxLayout:
            orientation:"vertical"
            size_hint:1,.5
            pos_hint:{"center_x":.5,"center_y":.5}
            Label:
                text:"psi"
                font_size:self.height/1.5
                color:root.warna_name
            Label:
                text:str(root.value)
                font_size:self.height*1.15
                color:root.warna_value
            Label:
    FloatLayout:
        size_hint: None, None
        pos_hint: {"center_x":0.5, "center_y":0.5}
        size: .94*min(root.size), .94*min(root.size)
        canvas:
            Color:
                rgba: root.warna_alpa
            Ellipse:
                size: self.size     
                pos: self.pos
                source:"asset/green_bolong.png"
                angle_start:219
                angle_end:220+280
    Image:
        pos_hint:{"center_x":.5,"center_y":.5}
        source:"asset/pucuk.png"
        size_hint:1.15,1.15
        color:1,0,0,1
        canvas.before:
            PushMatrix
            Rotate:
                angle: 320-root.anime_max_value*280/80
                origin: self.center
        canvas.after:
            PopMatrix
    FloatLayout:
        size_hint: None, None
        pos_hint: {"center_x":0.5, "center_y":0.5}
        size: .94*min(root.size), .94*min(root.size)
        canvas:
            Color:
                rgba: 1,1,1,.1
            Ellipse:
                size: self.size     
                pos: self.pos
                source:"asset/moon.png"
                angle_start:219
                angle_end:220+root.anime_value*280/80
    Image:
        color:1,1,1,.85
        source:"asset/jarum_putih.png"
        size_hint:.7,.7
        pos_hint: {"center_x":0.5, "center_y":0.5}
        canvas.before:
            PushMatrix
            Rotate:
                angle: 140-root.anime_value*280/80
                origin: self.center
        canvas.after:
            PopMatrix
   

<DialSpeed>:
    Image:
        source:"asset/speed.png"
        size_hint:1,1
        pos_hint: {"center_x":0.5, "center_y":0.5}
        color:root.warna
    FloatLayout:
        size_hint: None, None
        pos_hint: {"center_x":0.5, "center_y":0.5}
        size: .95*min(root.size), .95*min(root.size)
        canvas:
            Color:
                rgba: root.warna_alpa
            Ellipse:
                size: self.size     
                pos: self.pos
                source:"asset/green_bolong_bg.png"
                angle_start:219
                angle_end:220+root.anime_value*280/180
        BoxLayout:
            orientation:"vertical"
            size_hint:1,.5
            pos_hint:{"center_x":.5,"center_y":.5}
            Label:
                text:"kph"
                font_size:self.height/1.5
                color:root.warna_name
            Label:
                text:str(root.value)
                font_size:self.height*1.15
                color:root.warna_value
            Label:
    FloatLayout:
        size_hint: None, None
        pos_hint: {"center_x":0.5, "center_y":0.5}
        size: .94*min(root.size), .94*min(root.size)
        canvas:
            Color:
                rgba: root.warna_alpa
            Ellipse:
                size: self.size     
                pos: self.pos
                source:"asset/green_bolong.png"
                angle_start:219
                angle_end:220+280
    Image:
        pos_hint:{"center_x":.5,"center_y":.5}
        source:"asset/pucuk.png"
        size_hint:1.15,1.15
        color:1,0,0,1
        canvas.before:
            PushMatrix
            Rotate:
                angle: 320-root.anime_max_value*280/180
                origin: self.center
        canvas.after:
            PopMatrix
    FloatLayout:
        size_hint: None, None
        pos_hint: {"center_x":0.5, "center_y":0.5}
        size: .94*min(root.size), .94*min(root.size)
        canvas:
            Color:
                rgba: 1,1,1,.1
            Ellipse:
                size: self.size     
                pos: self.pos
                source:"asset/moon.png"
                angle_start:219
                angle_end:220+root.anime_value*280/180
    Image:
        
        color:1,1,1,.85
        source:"asset/jarum_putih.png"
        size_hint:.7,.7
        pos_hint: {"center_x":0.5, "center_y":0.5}
        canvas.before:
            PushMatrix
            Rotate:
                angle: 140-root.anime_value*280/180
                origin: self.center
        canvas.after:
            PopMatrix

<PsiScreen>:
    name:"psi"
    BoxLayout:
        spacing:5
        orientation:"vertical"
        FloatLayout:
            size_hint:1,None
            height:"300sp"
            pos_hint:{"center_x":.5,"center_y":.5}
            DialPressure:
                pos_hint:{"center_x":.5,"center_y":.5}
                id:psi
        Label:
            size_hint:1,None
            height:"30sp"
        Label:
            size_hint:1,None
            height:"30sp"
            text_size:self.size
            text:"sooko.io"
            color:1,1,1,.5
            font_size:self.height
        Button
            background_color:0,0,0,0
            canvas.before:
                Color:
                    rgba:0,1,1,.8
                RoundedRectangle:
                    size:self.size
                    pos:self.pos
                    source:"asset/gradient_blue.png"
            text:"  Pressure Gauge"
            color:0,0,0,1
            font_size:self.height/2
            size_hint:1,None
            pos_hint:{"right":1}
            height:"50sp"
            halign:"left"
            valign:"middle"
            text_size:self.size
        FloatLayout:
            id:flt
            size_hint:1,1
            pos_hint:{"center_x":.5,"center_y":.5}

""")
class DialTacho(FloatLayout):
    value = NumericProperty(0)
    max_value = NumericProperty(0)
    dial_text_color = ListProperty([0, 1, 1, .8])
    rainbow_color = ListProperty([0, 1, 1, .8])
    pucuk_color = ListProperty([0, 1, 0, 1])
    anime_value = NumericProperty(0)
    anime_max_value = NumericProperty(0)
    satuan = StringProperty("PRM")
    warna= ListProperty([0, 1, 1, 1])
    warna_name= ListProperty([0, 1, 1, 1])
    warna_value= ListProperty([0, 1, 1, 1])
    warna_alpa=ListProperty([0, 1, 1,.3])
    def __init__(self, *args, **kwargs):
        super(DialTacho, self).__init__(*args, **kwargs)
        self.demo()
    def demo(self):
        self.value = 14000
        if self.max_value < self.value:
            self.max_value = self.value
        self.anim = Animation(anime_value=self.value, duration=1)
        self.anim_max = Animation(anime_max_value=self.max_value, duration=1.5)
        self.anim.start(self)
        self.anim_max.start(self)
        Clock.schedule_once(self.delay_demo,2)
    def delay_demo(self,dt):
        self.value=0
        self.max_value=0
        self.anim = Animation(anime_value=self.value, duration=2)
        self.anim_max = Animation(anime_max_value=self.max_value, duration=2)
        self.anim.start(self)
        self.anim_max.start(self)
    def show_value(self,data):
        self.value=data
        if self.max_value<self.value:
            self.max_value=self.value
        self.anim = Animation(anime_value=self.value,duration=1,t="linear")
        self.anim_max=Animation(anime_max_value=self.max_value,duration=1,t="linear")
        self.anim.start(self)
        self.anim_max.start(self)
    def reset(self):
        self.anime_value = 0
        self.anime_max_value=0
        self.value = 0
        self.max_value = 0

class DialPressure(FloatLayout):
    value = NumericProperty(0)
    max_value = NumericProperty(0)
    dial_text_color = ListProperty([0, 1, 1, .8])
    rainbow_color = ListProperty([0, 1, 1, .8])
    pucuk_color = ListProperty([0, 1, 0, 1])
    anime_value = NumericProperty(0)
    anime_max_value = NumericProperty(0)
    satuan = StringProperty("PRM")
    warna= ListProperty([0, 1, 1, 1])
    warna_name= ListProperty([0, 1, 1, 1])
    warna_value= ListProperty([0, 1, 1, 1])
    warna_alpa=ListProperty([0, 1, 1,.3])
    def __init__(self, *args, **kwargs):
        super(DialPressure, self).__init__(*args, **kwargs)
        self.demo()
    def demo(self):
        self.value = 80
        if self.max_value < self.value:
            self.max_value = self.value
        self.anim = Animation(anime_value=self.value, duration=1)
        self.anim_max = Animation(anime_max_value=self.max_value, duration=1.5)
        self.anim.start(self)
        self.anim_max.start(self)
        Clock.schedule_once(self.delay_demo,2)
    def delay_demo(self,dt):
        self.value=0
        self.max_value=0
        self.anim = Animation(anime_value=self.value, duration=2)
        self.anim_max = Animation(anime_max_value=self.max_value, duration=2)
        self.anim.start(self)
        self.anim_max.start(self)
    def show_value(self,data):
        self.value=data
        if self.max_value<self.value:
            self.max_value=self.value
        self.anim = Animation(anime_value=self.value,duration=1,t="linear")
        self.anim_max=Animation(anime_max_value=self.max_value,duration=1,t="linear")
        self.anim.start(self)
        self.anim_max.start(self)
    def reset(self):
        self.anime_value = 0
        self.anime_max_value=0
        self.value = 0
        self.max_value = 0
class DialSpeed(FloatLayout):
    value = NumericProperty(0)
    max_value = NumericProperty(0)
    dial_text_color = ListProperty([0, 1, 1, .8])
    rainbow_color = ListProperty([0, 1, 1, .8])
    pucuk_color = ListProperty([0, 1, 0, 1])
    anime_value = NumericProperty(0)
    anime_max_value = NumericProperty(0)
    satuan = StringProperty("PRM")
    warna= ListProperty([0, 1, 1, 1])
    warna_name= ListProperty([0, 1, 1, 1])
    warna_value= ListProperty([0, 1, 1, 1])
    warna_alpa=ListProperty([0, 1, 1,.3])
    def __init__(self, *args, **kwargs):
        super(DialSpeed, self).__init__(*args, **kwargs)
        self.demo()
    def demo(self):
        self.value = 180
        if self.max_value < self.value:
            self.max_value = self.value
        self.anim = Animation(anime_value=self.value, duration=1)
        self.anim_max = Animation(anime_max_value=self.max_value, duration=1.5)
        self.anim.start(self)
        self.anim_max.start(self)
        Clock.schedule_once(self.delay_demo,2)
    def delay_demo(self,dt):
        self.value=0
        self.max_value=0
        self.anim = Animation(anime_value=self.value, duration=2)
        self.anim_max = Animation(anime_max_value=self.max_value, duration=2)
        self.anim.start(self)
        self.anim_max.start(self)
    def show_value(self,data):
        self.value=data
        if self.max_value<self.value:
            self.max_value=self.value
        self.anim = Animation(anime_value=self.value,duration=1,t="linear")
        self.anim_max=Animation(anime_max_value=self.max_value,duration=1,t="linear")
        self.anim.start(self)
        self.anim_max.start(self)
    def reset(self):
        self.anime_value = 0
        self.anime_max_value=0
        self.value = 0
        self.max_value = 0
class Sm(ScreenManager):
    pass
class PsiScreen(Screen):
    graph = Graph(xlabel=' ', ylabel='', x_ticks_minor=5,
                  x_ticks_major=0,
                  y_ticks_major=10,
                  y_ticks_minor=2,
                  y_grid_label=True, x_grid_label=False, padding=5,
                  x_grid=True, y_grid=True,
                  xmin=-0,
                  xmax=50,
                  ymin=0,
                  ymax=100,
                  label_options={'color': [0, 1, 1, 1], 'bold': False},
                  border_color=[0, 1, 1, .1],
                  tick_color=[1, 1, 1, 1])
    plot = LinePlot(color=[1, 0, 0, 1], line_width=1.5)
    plot.points = [(0, 0)]
    graph.add_plot(plot)
    clock = Clock
    def __init__(self, *args, **kwargs):
        super(PsiScreen, self).__init__(*args, **kwargs)
        self.ids["flt"].add_widget(self.graph)






# class MyApp(App):
#     sm=Sm()
#     def build(self):
#         self.sm.add_widget(PsiScreen())
#         return self.sm
# if __name__=="__main__":
#     MyApp().run()
