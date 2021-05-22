from rover_mission.objects.rover import Rover
from rover_mission.constants.params import DIRECTIONS, MOVEMENTS, EMPTY_CELL
from rover_mission.objects import mars


class LandingProhibited(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def land_rover(rover, mars_grid):
    try:
        assert isinstance(rover, Rover)
    except AssertionError:
        raise TypeError(f'Invalid rover object {type(rover)}')
    else:
        rover_x = rover.x
        rover_y = rover.y
        rover_id = rover.id

    try:
        assert isinstance(mars_grid, mars.Mars2DGrid)
    except AssertionError:
        raise TypeError(f'Invalid grid object {type(mars_grid)}')

    try:
        assert mars_grid.grid[rover_x, rover_y] == EMPTY_CELL
        mars_grid.grid[rover_x, rover_y] = rover_id
    except AssertionError:
        raise LandingProhibited('Landing location occupied')
    except IndexError:
        raise LandingProhibited('Landing location outside the grid')
