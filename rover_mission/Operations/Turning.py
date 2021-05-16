from rover_mission.constants.params import ROTATIONS, DIRECTIONS
from rover_mission.Objects.rover import Rover


class TurningError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


def change_direction(moves, rover):
    try:
        assert moves in ROTATIONS[0:2]
    except AssertionError:
        raise TypeError(f'Invalid turn instruction {moves} : can only be {ROTATIONS[0:2]}')

    try:
        assert isinstance(rover, Rover)
    except AssertionError:
        raise TypeError(f'Invalid rover object {type(rover)}')

    if moves == ROTATIONS[0]:
        rover.d = DIRECTIONS[DIRECTIONS.index(rover.d) - 1]
    if moves == ROTATIONS[1]:
        if (DIRECTIONS.index(rover.d) >= 3):
            rover.d = DIRECTIONS[0]
        else:
            rover.d = DIRECTIONS[DIRECTIONS.index(rover.d) + 1]
