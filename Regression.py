import math as m
import numpy as np
from scipy.optimize import curve_fit

class Regression:
    def __init__(self, x, y, yerr, func):
        self.x = x
        self.y = y
        self.yerr = yerr
        self.func = func
        self.popt = None
        self.pcov = None
        self.perr = None

    def fit_data(self):
        self.popt, self.pcov = curve_fit(self.func, self.x, self.y)
        self.perr = np.sqrt(np.diag(self.pcov))
    