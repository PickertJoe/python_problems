# A test function for the tiling cost calculator

import unittest
from tiling_cost_calculator import room_calculate, show_results


class CostTestCase(unittest.TestCase):
    """Tests the accuracy of the tiling cost calculator for a three room house"""

    def test_bathroom(self):
        """Will the calculator produce the appropriate answer and store it in the array?"""
        array = []
        array = room_calculate(10.5, 22.8, 19.76, array)
        self.assertEqual(array[0], 4730.544)


unittest.main()
