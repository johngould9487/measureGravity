import numpy as np

class File:
    def __init__(self, path):
        self.path = path

    def read_x_y_values_from_file(self):
        values = [[],[],[]]
        f = open(self.path, "r")
        for line in f:
            xyPair = line.split(',')
            values[0].append(float(xyPair[0]))
            values[1].append(float(xyPair[1]))
            values[2].append(float(xyPair[2]))
        f.close()
        return values[0], values[1], values[2]
