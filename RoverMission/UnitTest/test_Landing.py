import unittest
from RoverMission.Operations import Landing
from RoverMission.Objects import Rover, Mars

class TestLandingOperation(unittest.TestCase):
    def setUp(self):
        # Load test data
        self.mars_grid = Mars.Mars2DGrid(4,5)
        self.rover_on_grid = Rover.Rover(2,3,'N')
        self.rover_off_grid = Rover.Rover(6,2,'N')

    def test_type(self):
        #test for type of parameters
        self.assertRaises(TypeError,Landing.land_rover,'abcd','y')

    def test_off_grid_landing(self):
        self.assertRaises(Landing.LandingProhibited,Landing.land_rover, self.rover_off_grid, self.mars_grid)

    def test_on_grid_landing(self):
        Landing.land_rover(self.rover_on_grid,self.mars_grid)
        self.assertEqual(self.mars_grid.grid[self.rover_on_grid.x][self.rover_on_grid.y],1)