from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from dial import DialPressure
Builder.load_string('''
<PressureScreen>
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


''')

class PressureScreen(Screen):
    pass