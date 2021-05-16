from rover_mission.objects.rover import Rover
from rover_mission.constants.params import DIRECTIONS
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

    try:
        assert isinstance(mars_grid, mars.Mars2DGrid)
    except AssertionError:
        raise TypeError(f'Invalid grid object {type(mars_grid)}')

    if rover.d not in DIRECTIONS:
        raise LandingProhibited(
            f'Rover face direction {rover.d} in not in: {DIRECTIONS}')
    else:
        try:
            assert mars_grid.grid[rover.x, rover.y] == 0
            mars_grid.grid[rover.x, rover.y] = 1
        except AssertionError:
            raise LandingProhibited('Landing location occupied')
        except IndexError:
            raise LandingProhibited('Landing location outside the grid')
