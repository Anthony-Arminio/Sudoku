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
                self.reduceOptions(cell)
        print("")
        print(self.grid)

        self.stop = False
        while not self.stop:
            gridCopy = deepcopy(self.grid)
            self.stop = True
            for cell in range(81):
                for value in gridCopy[cell]:
                    if not self.isValid(deepcopy(gridCopy), cell, value):
                        self.grid[cell].remove(value)
                        self.stop = False
        print("")
        print(self.grid)
    
    def reduceOptions(self, cell):
        options = copy(self.grid[cell])
        for value in options:
            for testCell in range(81):
                if self.sees(cell, testCell):
                    if len(self.grid[testCell]) == 1 and self.grid[testCell][0] == value:
                        self.grid[cell].remove(value)
                        self.stop = False
                        break
    
    def isValid(self, grid, cell, value): # don't use self.grid in this function
        if self.isContradiction(grid, cell, value):
            return False
        newGrid = copy(grid)
        newGrid[cell] = [value]
        if cell + 1 < 81:
            for value in newGrid[cell + 1]:
                if self.isValid(copy(newGrid), cell + 1, value):
                    return True
            return False
        return True


    def isContradiction(self, grid, cell, value):
        for testCell in range(81):
            if self.sees(cell, testCell):
                if len(grid[testCell]) == 1 and grid[testCell][0] == value:
                    return True


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

# "937485020460273059852100734324790508710854302580021497605910273178602045293047601"