import unittest
from rover_mission.operations import moving, turning, landing
from rover_mission.objects.rover import Rover
from rover_mission.objects import mars
from rover_mission.constants.params import EMPTY_CELL


class TestMovingOperation(unittest.TestCase):
    def setUp(self):
        # Load test data
        self.mars_grid = mars.Mars2DGrid(4, 5)
        self.rover = Rover(2, 3, 'N', 1)
        landing.land_rover(self.rover, self.mars_grid)

    def test_type(self):
        # test for type of parameters
        self.assertRaises(TypeError, moving.change_position, 'abcd', 'y')

    def test_move_north(self):
        moving.change_position(self.rover, self.mars_grid)
        self.assertEqual(self.mars_grid.grid[1][2], EMPTY_CELL)
        self.assertEqual(self.mars_grid.grid[1][3], '1↑')

    def test_move_east(self):
        turning.change_direction('R', self.rover, self.mars_grid)
        moving.change_position(self.rover, self.mars_grid)
        self.assertEqual(self.mars_grid.grid[1][2], EMPTY_CELL)
        self.assertEqual(self.mars_grid.grid[2][2], '1→')

    def test_move_west(self):
        turning.change_direction('L', self.rover, self.mars_grid)
        moving.change_position(self.rover, self.mars_grid)
        self.assertEqual(self.mars_grid.grid[1][2], EMPTY_CELL)
        self.assertEqual(self.mars_grid.grid[0][2], '1←')

    def test_move_south(self):
        turning.change_direction('L', self.rover, self.mars_grid)
        turning.change_direction('L', self.rover, self.mars_grid)
        moving.change_position(self.rover, self.mars_grid)
        self.assertEqual(self.mars_grid.grid[1][2], EMPTY_CELL)
        self.assertEqual(self.mars_grid.grid[1][1], '1↓')
