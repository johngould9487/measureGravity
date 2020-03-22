import Graph as g
import File as f
import Regression as r
import numpy as np

def func(l, g):
    return np.power(g, 0.5) * np.power(l, -0.5)

file = f.File("data.csv")
x, y, yerr = file.read_x_y_values_from_file()
regression = r.Regression(x, y, yerr, func)
regression.fit_data()
graph = g.Graph(x, y, yerr, func, regression.popt[0])
graph.title = r'Calculating $g$ through measuring the period of a pendulum'
graph.x_caption = r'Length of pendulum $l/\textrm{m}$'
graph.y_caption = r'Angular frequency of pendulum $\omega /\textrm{s}^{-1}$'
graph.text = r'$g = ' + str(graph.g) + r' \pm 0.06$'
graph.text_x = 0.35
graph.text_y = 7.5

graph.show_graph()