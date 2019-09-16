from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.garden.graph import Graph, MeshLinePlot,LinePlot
from kivy.uix.boxlayout import BoxLayout
from chart import Chart
Builder.load_string('''
<Labele@Label>:
    halign:"right"
    valign:"middle"
    text_size:self.size
<TabungMbok@FloatLayout>:
    pos_hint:{"center_x":.5,"center_y":.5}
    canvas:
        Color:
            rgba:0,1,1,.1
        Rectangle:
            size:self.size
            pos:self.pos
<Tabung@FloatLayout>:
    pos_hint:{"center_x":.5,"center_y":.5}
    canvas:
        Color:
            rgba:0,1,1,.4
        Rectangle:
            size:self.size
            pos:self.pos
            source:"asset/batang.png"

<Tabung1@Label>:
    size_hint:.7,1
    pos_hint:{"center_x":.5,"y":0}
    canvas:
        Color:
            rgba:0,1,1,.3
        Rectangle:
            size:self.size
            pos:self.pos
            
<ThrottlePage>:
    pos_hint:{"center_x":.5,"center_y":.5}
    orientation:"vertical"
    FloatLayout:
        id:ok
        pos_hint:{"center_x":.5,"center_y":.5}
        BoxLayout:
            padding:20,0,20,0
            spacing:10
            pos_hint:{"center_x":.5,"center_y":.5}
           
            TabungMbok
                Tabung1  
                Tabung:
            TabungMbok
                Tabung1  
                Tabung:
            TabungMbok
                Tabung1  
                Tabung:
            TabungMbok
                Tabung1  
                Tabung:
                    
                               
            
        Chart
            pos_hint:{"center_x":.5,"center_y":.5}
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
        size_hint:1,.05
        padding:20,0,20,0
        spacing:10
        Label:
            color:0,1,1,1
            text:"120"
            font_size:self.height
        Label:
            color:0,1,1,1
            font_size:self.height
            text:"120"
        Label:
            color:0,1,1,1
            font_size:self.height
            text:"120"
        Label:
            color:0,1,1,1
            font_size:self.height
            text:"120"
        
    BoxLayout:
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

class ThrottlePage(BoxLayout):
    plot_cyl1 = LinePlot(color=[1, 0, 0, 1], line_width=25)
    plot_cyl2 = LinePlot(color=[1, 0, 0, 1], line_width=25)
    plot_cyl3 = LinePlot(color=[1, 0, 0, 1], line_width=25)
    plot_cyl4 = LinePlot(color=[1, 0, 0, 1], line_width=25)

    def __init__(self,*args,**kwargs):
        super(ThrottlePage,self).__init__(**kwargs)
        self.plot_cyl1.points=[(1.5,0),(1.5,10)]
        self.plot_cyl2.points=[(3.5,0),(3.5,10)]
        self.plot_cyl3.points=[(5.5,0),(5.5,10)]
        self.plot_cyl4.points=[(7.5,0),(7.5,10)]

        #
        #
        # self.ids["chart"].add_plot(self.plot_cyl1)
        # self.ids["chart"].add_plot(self.plot_cyl2)
        # self.ids["chart"].add_plot(self.plot_cyl3)
        # self.ids["chart"].add_plot(self.plot_cyl4)
        #
        #




