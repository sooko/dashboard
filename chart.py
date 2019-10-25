from kivy.garden.graph import Graph, MeshLinePlot,LinePlot
from kivy.properties import StringProperty,NumericProperty,ListProperty,BooleanProperty,DictProperty
class ChartPressure(Graph):
    poin=ListProperty([])
    xlabel=StringProperty("")
    ylabel=StringProperty("")
    x_ticks_minor=NumericProperty(0)
    x_ticks_major=NumericProperty(10)
    y_ticks_major=NumericProperty(10)
    y_ticks_minor=NumericProperty(2)
    y_grid_label=BooleanProperty(True)
    x_grid_label=BooleanProperty(False)
    x_grid=BooleanProperty(False)
    y_grid=BooleanProperty(True)
    xmin=NumericProperty(0)
    xmax=NumericProperty(50)
    ymin=NumericProperty(0)
    ymax=NumericProperty(100)
    label_options = DictProperty({'color': [0,1,1,1], 'bold':False})
    border_color = ListProperty([0,1,1,.1])
    tick_color = ListProperty([1,1,1,1])
    plot_pressure = LinePlot(color=[1, 0, 0, 1],line_width=1.5)
    plot_batt = LinePlot(color=[1,1, 0, 1],line_width=1.5)
    plot_pressure.points = [(0,0)]
    plot_batt.points = [(0,0)]
    def __init__(self,*args,**kwargs):
        super(ChartPressure,self).__init__(*args,**kwargs)
        self.add_plot(self.plot_pressure)
        self.add_plot(self.plot_batt)
    def show_chart_pressure(self,x_value,y_value):
        self.plot_pressure.points.append((x_value,y_value))
        if x_value>50:
            self.xmax+=1
            self.xmin+=1
            # self.plot_pressure.points.remove(self.plot_pressure.points[0])
        if x_value >55:
            self.plot_pressure.points.remove(self.plot_pressure.points[0])
    def show_chart_batt(self,x_value,y_value):
        self.plot_batt.points.append((x_value, y_value))

class ChartThrottle(Graph):
    poin=ListProperty([])
    xlabel=StringProperty("")
    ylabel=StringProperty("")
    x_ticks_minor=NumericProperty(0)
    x_ticks_major=NumericProperty(10)
    y_ticks_major=NumericProperty(10)
    y_ticks_minor=NumericProperty(2)
    y_grid_label=BooleanProperty(True)
    x_grid_label=BooleanProperty(False)
    x_grid=BooleanProperty(False)
    y_grid=BooleanProperty(True)
    xmin=NumericProperty(0)
    xmax=NumericProperty(50)
    ymin=NumericProperty(0)
    ymax=NumericProperty(100)
    label_options = DictProperty({'color': [0,1,1,1], 'bold':False})
    border_color = ListProperty([0,1,1,.1])
    tick_color = ListProperty([1,1,1,1])
    plot_pressure = LinePlot(color=[1, 0, 0, 1],line_width=1.5)
    plot_batt = LinePlot(color=[1,1, 0, 1],line_width=1.5)
    plot_pressure.points = [(0,0)]
    plot_batt.points = [(0,0)]
    def __init__(self,*args,**kwargs):
        super(ChartThrottle,self).__init__(*args,**kwargs)
        self.add_plot(self.plot_pressure)
        self.add_plot(self.plot_batt)
    # def show_chart_pressure(self,x_value,y_value):
    #     self.plot_pressure.points.append((x_value,y_value))
    #     if x_value>50:
    #         self.xmax+=1
    #         self.xmin+=1
    #     if x_value >55:
    #         self.plot_pressure.points.remove(self.plot_pressure.points[0])
    # def show_chart_batt(self,x_value,y_value):
    #     self.plot_batt.points.append((x_value, y_value))
    #
