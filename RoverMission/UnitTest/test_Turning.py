import unittest
from RoverMission.Operations import Turning
from RoverMission.Objects import Rover
from RoverMission.Constants.Parameters import directions

class TestTurningOperation(unittest.TestCase):
    def setUp(self):
        # Load test data
        self.rover = Rover.Rover(2,3,'N')

    def test_type(self):
        #test for type of parameters
        self.assertRaises(TypeError,Turning.change_direction,'abcd','y')

    def test_90_left_turn(self):
        Turning.change_direction('L',self.rover)
        self.assertEqual(self.rover.d,'W')
        
    def test_90_right_turn(self):
        Turning.change_direction('R',self.rover)
        self.assertEqual(self.rover.d,'E')

    def test_360_left_turn(self):
        Turning.change_direction('L',self.rover)
        Turning.change_direction('L',self.rover)
        Turning.change_direction('L',self.rover)
        Turning.change_direction('L',self.rover)
        self.assertEqual(self.rover.d,'N')
        
    def test_360_right_turn(self):
        Turning.change_direction('R',self.rover)
        Turning.change_direction('R',self.rover)
        Turning.change_direction('R',self.rover)
        Turning.change_direction('R',self.rover)
        self.assertEqual(self.rover.d,'N')
    