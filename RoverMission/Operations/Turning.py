from RoverMission.Constants.Parameters import rotations, directions
from RoverMission.Objects.Rover import Rover


class TurningError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


def change_direction(moves, rover):
    try:
        assert moves in rotations[0:2]
    except AssertionError:
        raise TypeError(f'Invalid turn instruction {moves} : can only be {rotations[0:2]}')

    try:
        assert isinstance(rover, Rover)
    except AssertionError:
        raise TypeError(f'Invalid rover object {type(rover)}')

    if moves == rotations[0]:
        rover.d = directions[directions.index(rover.d) - 1]
    if moves == rotations[1]:
        if (directions.index(rover.d) >= 3):
            rover.d = directions[0]
        else:
            rover.d = directions[directions.index(rover.d) + 1]
