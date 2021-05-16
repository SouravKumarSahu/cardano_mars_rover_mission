import unittest
from RoverMission.Objects import Mars


class TestMarsGridObject(unittest.TestCase):
    def test_type(self):
        #test for type of parameters
        self.assertRaises(TypeError,Mars.Mars2DGrid,'x','y')

    def test_initial_grid(self):
        mars_grid = Mars.Mars2DGrid(3,4)
        self.assertEqual(mars_grid.grid.sum(),0)

    def test_grid_shape(self):
        mars_grid = Mars.Mars2DGrid(6,4)
        self.assertEqual(mars_grid.grid.shape,(6,4))
    