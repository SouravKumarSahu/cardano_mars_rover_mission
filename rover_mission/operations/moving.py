from rover_mission.constants.params import MOVEMENTS, EMPTY_CELL
from rover_mission.objects import mars
from rover_mission.objects.rover import Rover


class MoveProhibited(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def change_position(rover, mars_grid):
    try:
        assert isinstance(rover, Rover)
    except AssertionError:
        raise TypeError(f'Invalid rover object {type(rover)}')
    else:
        rover_x = rover.x
        rover_y = rover.y
        rover_d = rover.d
        rover_id = rover.id

    try:
        assert isinstance(mars_grid, mars.Mars2DGrid)
    except AssertionError:
        raise TypeError(f'Invalid grid object {type(mars_grid)}')

    try:
        x, y = rover_x + \
            MOVEMENTS[rover_d][0][0], rover_y + MOVEMENTS[rover_d][0][1]
    except TypeError:
        raise MoveProhibited(f'Invalid movement value {MOVEMENTS[rover_d]}')

    try:
        assert 0 <= x <= mars_grid.grid.shape[0]
        assert 0 <= y <= mars_grid.grid.shape[1]
    except AssertionError:
        raise MoveProhibited(f'Rover {rover_id} will fall off grid')

    try:
        assert mars_grid.grid[x, y] == EMPTY_CELL
    except IndexError:
        raise MoveProhibited(f'Rover {rover_id} will fall off grid')
    except AssertionError:
        raise MoveProhibited(f"Rover {rover_id} can't move, path blocked")
    else:
        mars_grid.grid[x, y], mars_grid.grid[rover_x,
                                             rover_y] = rover_id, EMPTY_CELL
        rover.x, rover.y = x, y
