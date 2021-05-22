from rover_mission.constants.params import DIRECTIONS, MOVEMENTS


class RoverError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class Rover:
    def __init__(self, x, y, d, id):

        self._d, self._id, self._x, self._y, self._status, self._message = None, None, None, None, None, None

        self.d = d
        self.id = id

        try:
            self.x = int(x) - 1
            self.y = int(y) - 1
        except (TypeError, ValueError):
            raise TypeError(
                f'Rover landing X Y coordinate are not integer numbers: {x} x {y}')
        self.status = ""
        self.message = ""

    @property
    def d(self):
        return self._d

    @d.setter
    def d(self, val):
        try:
            assert val in DIRECTIONS
            self._d = val
        except AssertionError:
            raise TypeError(
                f'Rover direction {val} is not a part of: {DIRECTIONS}')

    @d.deleter
    def d(self):
        raise RoverError(f'Cannot delete the Direction of rover')

    @property
    def id(self):
        return str(self._id) + MOVEMENTS[self._d][1]

    @id.setter
    def id(self, val):
        self._id = val

    @id.deleter
    def id(self):
        raise RoverError(f'Cannot delete the ID of rover')

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        try:
            self._x = int(val)
        except (TypeError, ValueError):
            raise TypeError(
                f'Rover landing X coordinate is not integer numbers: x {val}')

    @x.deleter
    def x(self):
        raise RoverError(f'Cannot delete the X coordinate of rover')

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, val):
        try:
            self._y = int(val)
        except (TypeError, ValueError):
            raise TypeError(
                f'Rover landing Y coordinate is not integer numbers: y {val}')

    @y.deleter
    def y(self):
        raise RoverError(f'Cannot delete the Y coordinate of rover')

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, val):
        self._status = str(val)

    @status.deleter
    def status(self):
        raise RoverError(f'Cannot delete the Status of rover')

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, val):
        self._message = str(val)

    @message.deleter
    def message(self):
        raise RoverError(f'Cannot delete the Message of rover')

    def __str__(self):
        return str(self.x + 1) + " " + str(self.y + 1) + " " + str(self.d)
