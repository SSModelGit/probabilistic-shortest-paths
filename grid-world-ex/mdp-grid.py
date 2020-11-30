import numpy as np

class GridWorld:
    def __init__(self):
        self.grid = np.zeros([12,12],dtype=int) # For a grid of 10x10, pad on all sides to make 12x12
