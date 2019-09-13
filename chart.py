from kivy.garden.graph import Graph, MeshLinePlot,LinePlot
from kivy.properties import StringProperty,NumericProperty,ListProperty,BooleanProperty,DictProperty
class Chart(Graph):
    poin=ListProperty([])
    xlabel=StringProperty("")
    ylabel=StringProperty("")
    x_ticks_minor=NumericProperty(5)
    x_ticks_major=NumericProperty(0)
    y_ticks_major=NumericProperty(10)
    y_ticks_minor=NumericProperty(2)
    y_grid_label=BooleanProperty(True)
    x_grid_label=BooleanProperty(False)
    padding=NumericProperty(5)
    x_grid=BooleanProperty(True)
    y_grid=BooleanProperty(True)
    xmin=NumericProperty(0)
    xmax=NumericProperty(50)
    ymin=NumericProperty(0)
    ymax=NumericProperty(100)
    label_options = DictProperty({'color': [0,1,1,1], 'bold':False})
    border_color = ListProperty([0,1,1,.1])
    tick_color = ListProperty([1,1,1,1])
    plot = LinePlot(color=[1, 0, 0, 1],line_width=1.5)
    plot.points = [(0,0)]
    def __init__(self,*args,**kwargs):
        super(Chart,self).__init__(*args,**kwargs)
        self.add_plot(self.plot)
        self.plot.points=self.poin
    def show_chart(self,x_value,y_value):
        print("sho")




