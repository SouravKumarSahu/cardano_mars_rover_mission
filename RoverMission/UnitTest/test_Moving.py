import unittest
from RoverMission.Operations import Moving,Turning, Landing
from RoverMission.Objects import Rover, Mars

class TestMovingOperation(unittest.TestCase):
    def setUp(self):
        # Load test data
        self.mars_grid = Mars.Mars2DGrid(4,5)
        self.rover = Rover.Rover(2,3,'N')
        Landing.land_rover(self.rover,self.mars_grid)

    def test_type(self):
        #test for type of parameters
        self.assertRaises(TypeError,Moving.change_position,'abcd','y')

    def test_move_north(self):
        Moving.change_position(self.rover,self.mars_grid)
        self.assertEqual(self.mars_grid.grid[1][2],0)
        self.assertEqual(self.mars_grid.grid[1][3],1)

    def test_move_east(self):
        Turning.change_direction('R',self.rover)
        Moving.change_position(self.rover,self.mars_grid)
        self.assertEqual(self.mars_grid.grid[1][2],0)
        self.assertEqual(self.mars_grid.grid[2][2],1)

    def test_move_west(self):
        Turning.change_direction('L',self.rover)
        Moving.change_position(self.rover,self.mars_grid)
        self.assertEqual(self.mars_grid.grid[1][2],0)
        self.assertEqual(self.mars_grid.grid[0][2],1)
    
    def test_move_south(self):
        Turning.change_direction('L',self.rover)
        Turning.change_direction('L',self.rover)
        Moving.change_position(self.rover,self.mars_grid)
        self.assertEqual(self.mars_grid.grid[1][2],0)
        self.assertEqual(self.mars_grid.grid[1][1],1)
    
    