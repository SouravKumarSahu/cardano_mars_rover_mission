import unittest
from rover_mission.Operations import Landing
from rover_mission.Objects.rover import Rover
from rover_mission.Objects import mars

class TestLandingOperation(unittest.TestCase):
    def setUp(self):
        # Load test data
        self.mars_grid = mars.Mars2DGrid(4,5)
        self.rover_on_grid = Rover(2,3,'N')
        self.rover_off_grid = Rover(6,2,'N')

    def test_type(self):
        #test for type of parameters
        self.assertRaises(TypeError,Landing.land_rover,'abcd','y')

    def test_off_grid_landing(self):
        self.assertRaises(Landing.LandingProhibited,Landing.land_rover, self.rover_off_grid, self.mars_grid)

    def test_on_grid_landing(self):
        Landing.land_rover(self.rover_on_grid,self.mars_grid)
        self.assertEqual(self.mars_grid.grid[self.rover_on_grid.x][self.rover_on_grid.y],1)