import numpy as np
import math
from copy import copy
from copy import deepcopy

class Agent():
    def __init__(self, encodedGrid):
        self.grid = self.decodeGrid(encodedGrid)
        self.stop = False
        self.cancel = False
        self.solutions = []

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
        while not self.stop and not self.cancel:
            self.stop = True
            for cell in range(81):
                self.reduceOptions(cell)
        print("")
        print("Reduced Grid: ")
        self.printGrid(self.grid, 2)

        for value in self.grid[0]:
            if not self.isValid(deepcopy(self.grid), 0, value):
                pass
        
        print("")
        print("ALL SOLUTIONS: (Number of solutions: " + str(len(self.solutions)) + ")")
        for solution in self.solutions:
            self.printGrid(solution, 1)
            print("")
        print(len(self.solutions))
    
    def reduceOptions(self, cell):
        options = copy(self.grid[cell])
        for value in options:
            if self.isContradiction(self.grid, cell, value):
                self.grid[cell].remove(value)
                if len(self.grid[cell]) == 0:
                    self.cancel = True
                self.stop = False
                break
    
    def isValid(self, grid, cell, value): # don't use self.grid in this function
        if self.isContradiction(grid, cell, value):
            return False
        newGrid = copy(grid)
        newGrid[cell] = [value]
        if cell + 1 < 81:
            valid = False
            for value in newGrid[cell + 1]:
                if self.isValid(copy(newGrid), cell + 1, value):
                    valid = True
            if valid:
                return True
            else:
                return False
        else:
            print("")
            print("NEW SOLUTION FOUND: ")
            self.printGrid(newGrid, 1)
            self.solutions.append(copy(newGrid))
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

    def printGrid(self, grid, width):
        for cell in range(81):
            element = str(grid[cell])
            while len(element) < 3 * width:
                element += "   "
            print(element, end="")
            if cell % 9 == 8:
                print("")

solver = Agent("080600090100840000500000300002700000069000250000008600008000001000062005050004000")
solver.run()