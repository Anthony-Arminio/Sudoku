import numpy as np
import math
from copy import copy
from copy import deepcopy

class Agent():
    def __init__(self, encodedGrid):
        self.grid = self.decodeGrid(encodedGrid)
        self.stop = False

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
        while not self.stop:
            self.stop = True
            for cell in range(81):
                self.findValidOptions(deepcopy(self.grid), cell)
        print("")
        print(self.grid)
    
    def findValidOptions(self, grid, cell):
        options = copy(grid[cell])
        for value in options:
            for testCell in range(81):
                if self.sees(cell, testCell):
                    if len(self.grid[testCell]) == 1 and self.grid[testCell][0] == value:
                        self.grid[cell].remove(value)
                        self.stop = False
                        break

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

solver = Agent("907080000060203009850000004324790000700804002000021497600000073100602040000040601")
solver.run()

# "937485020460273059852100734324790508710854302580021497605910273178602045293047601"