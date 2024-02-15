from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.models import HoverTool
from bokeh.models.tickers import SingleIntervalTicker
from bokeh.palettes import Spectral11
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
import json

class GraphServer:
    def __init__(self):
        self.stats = self.read_stats()
        self.source = ColumnDataSource(data=dict(users=[], counts=[], percentages=[]))
        
        self.plot = figure(x_range=list(self.stats.keys()), 
                           height=350, 
                           sizing_mode='stretch_both', 
                           title="Overview", 
                           toolbar_location=None, 
                           tools="")
        

        self.plot.xgrid.grid_line_color = None
        self.plot.y_range.start = 0
        self.plot.yaxis.ticker = SingleIntervalTicker(interval=1)

        hover = HoverTool()
        hover.tooltips = [("", "@users"), ("", "@counts"), ("", "@percentages{0.2f}%")]
        self.plot.add_tools(hover)

        self.generate_vbar()


    def update(self):
        self.stats = self.read_stats()
        self.generate_vbar()
    
    def generate_vbar(self):
        users = list(self.stats.keys())
        counts = list(self.stats.values())
        percentages = [(count / sum(counts)) * 100 for count in counts]
        palette = Spectral11 * (len(users) // len(Spectral11) + 1)

        self.source.data = dict(users=users, counts=counts, percentages=percentages)
        self.plot.x_range.factors = users

        self.plot.vbar(x="users", 
                       top="counts", 
                       width=0.9, 
                       source=self.source, 
                       line_color=None, 
                       fill_color=factor_cmap('users', palette=palette, factors=users))


    def read_stats(self):
        try:
            with open("stats.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def start(self):
        curdoc().add_root(self.plot)
        curdoc().add_periodic_callback(self.update, 1000)


graph = GraphServer()
graph.start()