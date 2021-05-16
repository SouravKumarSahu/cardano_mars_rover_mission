import unittest
from rover_mission.Objects.rover import Rover


class TestMarsGridObject(unittest.TestCase):
    def test_type(self):
        #test for type of parameters
        self.assertRaises(TypeError,Rover,'x','y','N')

    def test_initial_rover(self):
        rover = Rover(3,4,'N')
        self.assertEqual(rover.__str__(),'3 4 N')

    
    