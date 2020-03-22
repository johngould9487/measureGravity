import numpy as np
import matplotlib
matplotlib.rcParams['text.usetex'] = True
from matplotlib import pyplot as plt

class Graph:
    def __init__(self, x, y, yerr, func, g):
        self.x = x
        self.y = y
        self.yerr = yerr
        self.func = func
        self.g = g
        self.title = ""
        self.x_caption = ""
        self.y_caption = ""
        self.text = ""
        self.text_x = 0
        self.text_y = 0

    def show_graph(self):
        x = np.array(self.x)
        y = np.array(self.y)
        yerr = np.array(self.yerr)

        xcalculated = np.linspace(self.x[0], self.x[-1])
        ycalculated = []
        for xval in xcalculated:
            ycalculated.append(self.func(xval, self.g))
        ycalculated = np.array(ycalculated)

        plt.title(self.title) 
        plt.xlabel(self.x_caption)
        plt.ylabel(self.y_caption) 
        plt.errorbar(x,y,yerr,ls="none")
        plt.grid()
        plt.text(self.text_x, self.text_y, self.text)
        plt.ticklabel_format(axis='y',style='sci',scilimits=(0,3))
        plt.plot(xcalculated, ycalculated)
        plt.show()