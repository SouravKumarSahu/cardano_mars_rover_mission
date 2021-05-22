import unittest
from rover_mission.objects import mars
from rover_mission.constants.params import EMPTY_CELL
import numpy as np


class TestMarsGridObject(unittest.TestCase):
    def test_type(self):
        # test for type of parameters
        self.assertRaises(TypeError, mars.Mars2DGrid, 'x', 'y')

    def test_initial_grid(self):
        mars_grid = mars.Mars2DGrid(3, 4)
        test_grid = grid = np.array(
            [[EMPTY_CELL for a in range(4)] for a in range(3)])
        comparison = mars_grid.grid == test_grid
        self.assertEqual(comparison.all(), True)

    def test_grid_shape(self):
        mars_grid = mars.Mars2DGrid(6, 4)
        self.assertEqual(mars_grid.grid.shape, (6, 4))
