from RoverMission.Constants.Parameters import movements
from RoverMission.Objects import Rover, Mars


class MoveProhibited(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def change_position(rover, mars_grid):
    try:
        assert isinstance(rover, Rover.Rover)
    except AssertionError:
        raise TypeError(f'Invalid rover object {type(rover)}')

    try:
        assert isinstance(mars_grid, Mars.Mars2DGrid)
    except AssertionError:
        raise TypeError(f'Invalid grid object {type(mars_grid)}')

    try:
        x, y = rover.x + movements[rover.d][0], rover.y + movements[rover.d][1]
    except TypeError:
        raise MoveProhibited(f'Invalid movement value {movements[rover.d]}')
    
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
