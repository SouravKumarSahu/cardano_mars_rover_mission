from rover_mission.constants.params import DIRECTIONS


class RoverError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class Rover:
    def __init__(self, x, y, d):
        try:
            self.x = int(x) - 1
            self.y = int(y) - 1
        except (TypeError, ValueError):
            raise TypeError(
                f'Rover landing coordinates are not integer numbers: {x} x {y}')

        try:
            assert d in DIRECTIONS
            self.d = d
        except AssertionError:
            raise TypeError(
                f'Rover direction {d} is not a part of: {DIRECTIONS}')

        self.status = None
        self.message = None

    def __str__(self):
        return str(self.x + 1) + " " + str(self.y + 1) + " " + self.d
