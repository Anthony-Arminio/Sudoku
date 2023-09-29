import numpy as np
import math
from copy import copy

class Agent():
    def __init__(self, encodedGrid):
        self.grid = self.decodeGrid(encodedGrid)

    def decodeGrid(self, encodedGrid):
        grid = []
        for digit in encodedGrid:
            if digit == "0":
                grid.append([1, 2, 3, 4, 5, 6, 7, 8, 9])
            else:
                grid.append([int(digit)])
        print(grid)
        return grid
    
    def run(self):
        for cell in range(81):
            self.findValidOptions(self.grid, cell)
    
    def findValidOptions(self, grid, cell):
        pass
            


    def sees(self, cell1, cell2):
        if cell1 == cell2:
            return False

        # same row
        if math.floor(cell1 / 9) == math.floor(cell2 / 9):
            return True

        # same column
        if cell1 % 9 == cell2 % 9:
            return True
        
        # same box
        if math.floor(cell1 / 27) == math.floor(cell2 / 27) and math.floor((cell1 % 9) / 3) == math.floor((cell2 % 9) / 3):
            return True
        
        return False

solver = Agent("080600090100840000500000300002700000069000250000008600008000001000062005050004030")
solver.run()