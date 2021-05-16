from rover_mission.constants.params import MOVEMENTS
from rover_mission.Objects import mars
from rover_mission.Objects.rover import Rover


class MoveProhibited(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def change_position(rover, mars_grid):
    try:
        assert isinstance(rover, Rover)
    except AssertionError:
        raise TypeError(f'Invalid rover object {type(rover)}')

    try:
        assert isinstance(mars_grid, mars.Mars2DGrid)
    except AssertionError:
        raise TypeError(f'Invalid grid object {type(mars_grid)}')

    try:
        x, y = rover.x + MOVEMENTS[rover.d][0], rover.y + MOVEMENTS[rover.d][1]
    except TypeError:
        raise MoveProhibited(f'Invalid movement value {MOVEMENTS[rover.d]}')
    
    try:
        assert 0 <= x <= mars_grid.grid.shape[0]
        assert 0 <= y <= mars_grid.grid.shape[1]
    except AssertionError:
        raise MoveProhibited(f'Rover will fall off grid')
    
    
    try:
        assert mars_grid.grid[x, y] == 0
    except IndexError:
        raise MoveProhibited(f'Rover will fall off grid')
    except AssertionError:
        raise MoveProhibited(f"Rover can't move, path blocked")
    else:
        mars_grid.grid[x, y], mars_grid.grid[rover.x,
                                             rover.y] = mars_grid.grid[rover.x, rover.y], 0
        rover.x, rover.y = x, y
