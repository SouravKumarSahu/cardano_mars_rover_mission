import unittest
from rover_mission.operations import turning
from rover_mission.objects.rover import Rover

class TestTurningOperation(unittest.TestCase):
    def setUp(self):
        # Load test data
        self.rover = Rover(2,3,'N', 1)

    def test_type(self):
        #test for type of parameters
        self.assertRaises(TypeError,turning.change_direction,'abcd','y')

    def test_90_left_turn(self):
        turning.change_direction('L',self.rover)
        self.assertEqual(self.rover.d,'W')
        
    def test_90_right_turn(self):
        turning.change_direction('R',self.rover)
        self.assertEqual(self.rover.d,'E')

    def test_360_left_turn(self):
        turning.change_direction('L',self.rover)
        turning.change_direction('L',self.rover)
        turning.change_direction('L',self.rover)
        turning.change_direction('L',self.rover)
        self.assertEqual(self.rover.d,'N')
        
    def test_360_right_turn(self):
        turning.change_direction('R',self.rover)
        turning.change_direction('R',self.rover)
        turning.change_direction('R',self.rover)
        turning.change_direction('R',self.rover)
        self.assertEqual(self.rover.d,'N')
    