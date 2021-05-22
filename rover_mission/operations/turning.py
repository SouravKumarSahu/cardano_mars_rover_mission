from rover_mission.constants.params import ROTATIONS, DIRECTIONS
from rover_mission.objects.rover import Rover


class TurningError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


def change_direction(moves, rover, mars_grid):
    try:
        assert moves in ROTATIONS[0:2]
    except AssertionError:
        raise TypeError(
            f'Invalid turn instruction {moves} : can only be {ROTATIONS[0:2]}')

    try:
        assert isinstance(rover, Rover)
    except AssertionError:
        raise TypeError(f'Invalid rover object {type(rover)}')
    else:
        rover_x = rover.x
        rover_y = rover.y
        rover_d = rover.d

    if moves == ROTATIONS[0]:
        rover.d = DIRECTIONS[DIRECTIONS.index(rover_d) - 1]

    if (moves == ROTATIONS[1]) and (DIRECTIONS.index(rover_d) >= 3):
        rover.d = DIRECTIONS[0]

    if (moves == ROTATIONS[1]) and (DIRECTIONS.index(rover_d) < 3):
        rover.d = DIRECTIONS[DIRECTIONS.index(rover_d) + 1]

    mars_grid.grid[rover_x, rover_y] = rover.id
