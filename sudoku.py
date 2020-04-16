
import time
import json
import numpy as np
import genetic_solver as gss


class Board():
    def __init__(self, file):
        self.easy, self.medium, self.hard, self.expert = [], [], [], []
        self.load_db(file)
        self.grid = np.array(list(self.easy[0])).reshape((9, 9)).astype(str)

    def load_db(self, file):
        with open(file) as f:
            data = json.load(f)
        self.easy = data['Easy']
        self.medium = data['Medium']
        self.hard = data['Hard']
        self.expert = data['Expert']

    def solver(self):
        s = gss.GA_Solver()
        s.load(self.easy[0])
        start_time = time.time()
        self.pretty_print(self.grid)
        generation, solution = s.solve()
        if (solution):
            if generation == -1:
                print("Invalid inputs")
            elif generation == -2:
                print("No solution found")
            else:
                time_elapsed = '{0:6.2f}'.format(time.time()-start_time)
                str_print = "Solution found at generation: " + str(generation) + \
                        "\n" + "Time elapsed: " + str(time_elapsed) + "s"
                self.pretty_print(solution.values)
                print(str_print)

    def pretty_print(self, grid):
        for i in range(len(grid)):
            if i % 3 == 0 and i != 0:
                print(" --------+---------+--------")
            for j in range(len(grid[0])):
                if j % 3 == 0 and j != 0:
                    print("|", end="")
                if j == 8:
                    print(' ' +str(grid[i][j]))
                else:
                    print(' ' + str(grid[i][j]) + ' ', end="")

s = Board("sudoku_samples.json")
s.solver()
