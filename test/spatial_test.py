#!/usr/bin/env python3
# Test file for TrajUtil class in python package homework2
# RKS

# Project imports
import homework2.spatial_utility as su

# Python imports
import unittest

# 3rd party imports

# Constants
PKG = 'homework2'

class BasicTestCase(unittest.TestCase):
    """
    Test Cases which check calulations at times:
    0 sec
    1 sec
    4.67 sec (random time)
    10 sec

    This is given the width = height = 1 and period = 10
    """
    def setUp(self):
        self.util = su.TrajUtil(width_m = 1, height_m = 1, period_s = 10)
        self.test_val1 = 0
        self.test_val2 = 1
        self.test_val3 = 4.67
        self.test_val4 = 10
        self.precision = 4

    def test_zero_all(self):
        self.assertEqual(
            np.around(self.util.get_x(self.test_val1), self.precision),
            np.around(0.0, self.precision))
        self.assertEqual(
            np.around(self.util.get_x_dot(self.test_val1), self.precision),
            np.around(0.314159, self.precision))
        self.assertEqual(
            np.around(self.util.get_x_ddot(self.test_val1), self.precision),
            np.around(0.0, self.precision))
        self.assertEqual(
            np.around(self.util.get_y(self.test_val1), self.precision),
            np.around(0.0, self.precision))
        self.assertEqual(
            np.around(self.util.get_y_dot(self.test_val1), self.precision),
            np.around(0.62831, self.precision))
        self.assertEqual(
            np.around(self.util.get_y_ddot(self.test_val1), self.precision),
            np.around(0.0, self.precision))
        self.assertEqual(
            np.around(self.util.get_linear_vel(self.test_val1), self.precision),
            np.around(0.702481, self.precision))
        self.assertEqual(
            np.around(self.util.get_rotational_vel(self.test_val1), self.precision),
            np.around(0.0, self.precision))

    def test_one_all(self):
        self.assertEqual(
            np.around(self.util.get_x(self.test_val2), self.precision),
            np.around(0.293892, self.precision))
        self.assertEqual(
            np.around(self.util.get_x_dot(self.test_val2), self.precision),
            np.around(0.2541601, self.precision))
        self.assertEqual(
            np.around(self.util.get_x_ddot(self.test_val2), self.precision),
            np.around(-0.116024, self.precision))
        self.assertEqual(
            np.around(self.util.get_y(self.test_val2), self.precision),
            np.around(0.4755282, self.precision))
        self.assertEqual(
            np.around(self.util.get_y_dot(self.test_val2), self.precision),
            np.around(0.194161, self.precision))
        self.assertEqual(
            np.around(self.util.get_y_ddot(self.test_val2), self.precision),
            np.around(-0.750924, self.precision))
        self.assertEqual(
            np.around(self.util.get_linear_vel(self.test_val2), self.precision),
            np.around(0.319837, self.precision))
        self.assertEqual(
            np.around(self.util.get_rotational_vel(self.test_val2), self.precision),
            np.around(-1.64549, self.precision))

    def test_random_val_all(self):
        self.assertEqual(
            np.around(self.util.get_x(self.test_val2), self.precision),
            np.around(0.102931, self.precision))
        self.assertEqual(
            np.around(self.util.get_x_dot(self.test_val2), self.precision),
            np.around(-0.307430, self.precision))
        self.assertEqual(
            np.around(self.util.get_x_ddot(self.test_val2), self.precision),
            np.around(-0.040635, self.precision))
        self.assertEqual(
            np.around(self.util.get_y(self.test_val2), self.precision),
            np.around(-0.201453, self.precision))
        self.assertEqual(
            np.around(self.util.get_y_dot(self.test_val2), self.precision),
            np.around(0.575062, self.precision))
        self.assertEqual(
            np.around(self.util.get_y_ddot(self.test_val2), self.precision),
            np.around(0.3181221, self.precision))
        self.assertEqual(
            np.around(self.util.get_linear_vel(self.test_val2), self.precision),
            np.around(0.6520819, self.precision))
        self.assertEqual(
            np.around(self.util.get_rotational_vel(self.test_val2), self.precision),
            np.around(-0.175048, self.precision))

    def test_full_cycle(self):
        # These test values should be the same test_zero_all
        self.assertEqual(
            np.around(self.util.get_x(self.test_val1), self.precision),
            np.around(0.0, self.precision))
        self.assertEqual(
            np.around(self.util.get_x_dot(self.test_val1), self.precision),
            np.around(0.314159, self.precision))
        self.assertEqual(
            np.around(self.util.get_x_ddot(self.test_val1), self.precision),
            np.around(0.0, self.precision))
        self.assertEqual(
            np.around(self.util.get_y(self.test_val1), self.precision),
            np.around(0.0, self.precision))
        self.assertEqual(
            np.around(self.util.get_y_dot(self.test_val1), self.precision),
            np.around(0.62831, self.precision))
        self.assertEqual(
            np.around(self.util.get_y_ddot(self.test_val1), self.precision),
            np.around(0.0, self.precision))
        self.assertEqual(
            np.around(self.util.get_linear_vel(self.test_val1), self.precision),
            np.around(0.702481, self.precision))
        self.assertEqual(
            np.around(self.util.get_rotational_vel(self.test_val1), self.precision),
            np.around(0.0, self.precision))

if __name__ == '__main__':
    import rosunit
    rosunit.unitrun(PKG, 'basic_test', BasicTestCase)

    