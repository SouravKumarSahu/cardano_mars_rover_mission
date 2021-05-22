import unittest
from rover_mission.objects.rover import Rover


class TestMarsGridObject(unittest.TestCase):
    def test_type(self):
        # test for type of parameters
        self.assertRaises(TypeError, Rover, 'x', 'y', 'N', 1)

    def test_initial_rover(self):
        rover = Rover(3, 4, 'N', 1)
        self.assertEqual(rover.__str__(), '3 4 N')
        self.assertEqual(rover.id, '1↑')
