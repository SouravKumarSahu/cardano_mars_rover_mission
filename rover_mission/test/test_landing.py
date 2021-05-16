import unittest
from rover_mission.operations import landing
from rover_mission.objects.rover import Rover
from rover_mission.objects import mars

class TestLandingOperation(unittest.TestCase):
    def setUp(self):
        # Load test data
        self.mars_grid = mars.Mars2DGrid(4,5)
        self.rover_on_grid = Rover(2,3,'N')
        self.rover_off_grid = Rover(6,2,'N')

    def test_type(self):
        #test for type of parameters
        self.assertRaises(TypeError,landing.land_rover,'abcd','y')

    def test_off_grid_landing(self):
        self.assertRaises(landing.LandingProhibited,landing.land_rover, self.rover_off_grid, self.mars_grid)

    def test_on_grid_landing(self):
        landing.land_rover(self.rover_on_grid,self.mars_grid)
        self.assertEqual(self.mars_grid.grid[self.rover_on_grid.x][self.rover_on_grid.y],1)