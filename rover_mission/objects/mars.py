import numpy as np


class MarsError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class Mars2DGrid:
    def __init__(self, x, y):
        try:
            self.x = int(x)
            self.y = int(y)
            self.grid = np.array([[0 for a in range(self.y)]
                                for a in range(self.x)])
        except (TypeError, ValueError):
            raise TypeError(f'Grid coordinates are not integer numbers: {x} x {y}')

    def __str__(self):
        t_grid = self.grid.transpose()
        print_grid = ""
        for i in range(self.y - 1, -1, -1):
            print_grid += str(t_grid[i]) + "\n"
        return print_grid
