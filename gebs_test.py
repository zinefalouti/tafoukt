import unittest
import numpy as np
from collections import defaultdict
from gebs import * 

class TestAlgorithms(unittest.TestCase):

    # Test that the mock matrix is generated correctly
    def test_mock_matrix_generation(self):
        rows, cols = 1300, 1300
        data = [[random.randint(0, 9) for _ in range(cols)] for _ in range(rows)]
        self.assertEqual(len(data), rows)
        self.assertEqual(len(data[0]), cols)

    # Test that 'overview' aggregates objectives correctly
    def test_overview(self):
        matched_objectives = [
            {'objective': 6, 'position': 0, 'area': 'Central Close Radius'},
            {'objective': 6, 'position': 1, 'area': 'Central Close Radius'},
            {'objective': 9, 'position': 2, 'area': 'Far Gradient Radius'},
            {'objective': 3, 'position': 3, 'area': 'Far Gradient Radius'},
        ]
        result = overview(matched_objectives)
        self.assertIn("Objective '6'", result)
        self.assertIn("Objective '9'", result)

    # Test the 'slicer' function for the correct number of slices
    def test_slicer(self):
        rows, cols = 1300, 1300
        data = np.random.randint(0, 10, (rows, cols))
        sliced_data, _ = slicer(data, (130, 130))
        self.assertEqual(len(sliced_data), 9)  # 9 slices expected

    # Test the 'sinusoidal' function with edge cases
    def test_sinusoidal(self):
        result = sinusoidal(0, 100, 0.2, 0.7)
        self.assertGreaterEqual(result, 0.13)
        self.assertLessEqual(result, 0.7)


if __name__ == '__main__':
    unittest.main()
