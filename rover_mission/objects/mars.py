import numpy as np
from rover_mission.constants.params import EMPTY_CELL


class MarsError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class Mars2DGrid:
    def __init__(self, x, y, empty_grid=EMPTY_CELL):
        self._x, self._y, self._grid = None, None, None

        self.x = x
        self.y = y
        self.grid = np.array([[empty_grid for a in range(self.y)]
                              for a in range(self.x)])

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        try:
            self._x = int(val)
        except (TypeError, ValueError):
            raise TypeError(f'Grid coordinate X is not integer number: {val}')

    @x.deleter
    def x(self):
        raise MarsError(f'Cannot delete the X coordinate of grid')

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, val):
        try:
            self._y = int(val)
        except (TypeError, ValueError):
            raise TypeError(f'Grid coordinate Y is not integer number: {val}')

    @y.deleter
    def y(self):
        raise MarsError(f'Cannot delete the Y coordinate of grid')

    def __str__(self):
        t_grid = self.grid.transpose()
        print_grid = ""
        for i in range(self.y - 1, -1, -1):
            print_grid += str(t_grid[i]) + "\n"
        return print_grid
