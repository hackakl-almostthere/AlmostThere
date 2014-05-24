import unittest

from User import User
from Stop import Stop

class Test_UserTest(unittest.TestCase):
    
    def setUp(self):
        self.user = User(-36.854134, 174.767841)
        self.stop = Stop(-36.843574, 174.766931)

    def test_Position(self):
        position = self.user.position
        
        # Tests the lattittude
        self.assertEqual(-36.854134, position[0])
        # Tests the longitude
        self.assertEqual(174.767841, position[1])

    def test_WalkingSpeed_Default(self):
        """
        Tests the default activity of the user
        """
        walkingSpeed = self.user.walkingSpeed

        self.assertEqual(4 / 3.6, walkingSpeed)

    def test_WalkingSpeed_Specified(self):
        """
        Tests the creation part of the user
        """
        user = User(-36.854134, 174.767841, 5)

        self.assertEqual(5 / 3.6, user.walkingSpeed)

    def test_calculate_distance_from_stop_at_starting_position(self):
        stop = Stop(-36.854134, 174.767841)

        distance = self.user.calculate_distance_from_stop(stop)

        self.assertEqual(distance, self.user.distance)

        self.assertEqual(distance, 0)

    def test_Calculate_Distance_from_stop_stop(self):
        expectedValue = 1178
        actualValue = self.user.calculate_distance_from_stop(self.stop)

        self.assertEqual(expectedValue, int(actualValue))

    def test_calculate_walking_time_from_starting_position(self):
        expectedValue = 0

        stop = Stop(-36.854134, 174.767841)
        actualValue = self.user.calculate_walking_time(stop)

        self.assertEqual(expectedValue, actualValue)
        
    def test_calculate_Walking_Time_from_stop(self):
        expectedValue = 2121

        actualValue = self.user.calculate_walking_time(self.stop)

        self.assertEqual(expectedValue, round(actualValue))

if __name__ == '__main__':
    unittest.main()
