import random
import time
import json
import numpy as np
import genetic_solver as gss


class Board():
    def __init__(self, level):
        with open('sudoku_samples.json') as f:
            data = json.load(f)
        self.easy = data['Easy']
        self.medium = data['Medium']
        self.hard = data['Hard']
        self.expert = data['Expert']
        if level == 'easy':
            self.rawData = self.easy[1]
        elif level == 'medium':
            self.rawData = self.medium[0]
        elif level == 'hard':
            self.rawData = self.hard[random.randint(0, 9)]
        elif level == 'expert':
            self.rawData = self.expert[random.randint(0, 9)]
        self.grid = np.array(list(self.rawData)).reshape((9, 9)).astype(str)

    def solve(self):
        s = gss.GA_Solver()
        s.load(self.rawData)
        start_time = time.time()
        self.pretty_print(self.grid)
        generation, solution, reseed = s.solve()
        if (solution):
            if generation == -1:
                print("Invalid inputs")
            elif generation == -2:
                print("No solution found")
            else:
                time_elapsed = time.time()-start_time
                str_print = "Solution found at generation: " + str(generation) + \
                        "\n" + "Time elapsed: " + str('{0:6.2f}'.format(time_elapsed)) + "s"
                print('============ Solution =============')
                self.pretty_print(solution.values)
                print(str_print)
                return generation, time_elapsed, reseed


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


total_generation = 0
total_time = 0
total_restart = 0
# b = Board('medium')
# b.solve()

for i in range(10):
    b = Board('medium')
    generation, time_cost, restart = b.solve()
    total_generation += generation
    total_time += time_cost
    total_restart += restart

print(total_generation/10, total_time/10, total_restart)