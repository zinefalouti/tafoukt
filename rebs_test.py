import unittest
import io
import sys
from collections import Counter

from rebs import (
    data,
    objectives,
    allin,
    overview,
    center,
    initialize,
    expand,
    expand_rythm,
    visualize,
    parseRaw,
    consumed,
    matches
)

class TestMyModule(unittest.TestCase):

    def setUp(self):
        # Reset the global state before each test.
        consumed.clear()
        matches.clear()
        # Use the provided mock data and objectives in the module.
        self.data = data
        self.objectives = objectives

    def tearDown(self):
        # Clear global variables after each test.
        consumed.clear()
        matches.clear()

    def test_center(self):
        """Test that the center function returns the correct matrix center."""
        result = center(self.data)
        expected = (len(self.data[0]) // 2, len(self.data) // 2)
        self.assertEqual(result, expected, "Center function did not return the expected coordinates.")

    def test_initialize(self):
        """Test that initialize adds matches and marks consumed cells correctly."""
        # Choose an arbitrary center (for example, the matrix center).
        c = center(self.data)
        # Use expansion vector (1,1) and full precision (1,1).
        initialize(self.data, self.objectives, c, (1, 1), 1, 1, debug=False)
        # Given the way initialize works:
        #  - It uses a width range:  x - int(1*1) to x + int(1*1)+1
        #  - And a height range: y - int(1*1) to y + int(1*1)+1.
        x, y = c
        expected_cols = range(x - 1, x + 2)
        expected_rows = range(y - 1, y + 2)
        # Check that every match is within the expected bounds.
        for m in matches:
            # m is a tuple: (value, col, row)
            self.assertIn(m[1], expected_cols, "Match column out of expected bounds.")
            self.assertIn(m[2], expected_rows, "Match row out of expected bounds.")
        # Also, every consumed coordinate should be in these ranges.
        for (row, col) in consumed:
            self.assertIn(col, expected_cols, "Consumed column out of expected bounds.")
            self.assertIn(row, expected_rows, "Consumed row out of expected bounds.")

    def test_expand(self):
        """Test that expand finds additional objectives around the center."""
        consumed.clear()
        matches.clear()
        # Choose a center arbitrarily.
        c = (5, 4)
        result = expand(self.data, self.objectives, c, (1, 1), 1, 1, debug=False)
        # The result is a list of objective values found in the new "crust" (cells not already consumed).
        self.assertIsInstance(result, list, "expand should return a list.")
        # Also, matches should have been updated.
        self.assertGreaterEqual(len(matches), len(result), "Global matches not updated properly by expand.")

    def test_expand_rythm(self):
        """Test that expand_rythm loops and expands the search area, updating matches."""
        consumed.clear()
        matches.clear()
        c = center(self.data)
        expand_rythm(self.data, self.objectives, c, (1, 1), 1, 1, debug=False)
        # After expansion, there should be some matches found.
        self.assertGreater(len(matches), 0, "expand_rythm did not add any matches.")

    def test_overview(self):
        """Test that overview returns counts of duplicates correctly."""
        # Manually populate matches with some duplicates.
        matches.clear()
        sample_matches = [
            (1, 2, 3),
            (1, 4, 5),
            (7, 1, 2),
            (7, 2, 2),
            (3, 0, 0)
        ]
        matches.extend(sample_matches)
        dupes = overview(matches)
        # Expect duplicates for values 1 and 7 (since each appears twice) but not for 3.
        self.assertEqual(dupes, {1: 2, 7: 2}, "overview did not return the expected duplicate counts.")

    def test_parseRaw(self):
        """Test that parseRaw returns all occurrences of objectives in the data."""
        result = parseRaw(self.data, self.objectives)
        # Manually compute expected result.
        expected = []
        for i, row in enumerate(self.data):
            for j, val in enumerate(row):
                if val in self.objectives:
                    expected.append((val, j, i))
        # Sort both lists for comparison.
        self.assertEqual(sorted(result), sorted(expected), "parseRaw did not return the expected list of tuples.")

    def test_allin(self):
        """Test that allin executes the search and returns matches."""
        matches.clear()
        result = allin(self.data, self.objectives, (1, 1), 1, 1, debug=False)
        # allin should return the same global matches list (non-empty if any objectives are found).
        self.assertEqual(result, matches, "allin did not return the global matches list.")
        self.assertGreater(len(result), 0, "allin returned an empty result list, expected some matches.")

    def test_visualize(self):
        """Test that visualize produces output (capture printed output)."""
        # Redirect stdout to capture visualize output.
        captured_output = io.StringIO()
        sys.stdout = captured_output
        c = center(self.data)
        # Provide a dummy matches list so that visualize prints something.
        dummy_matches = [(1, 2, 3)]
        visualize(self.data, c, dummy_matches)
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertTrue(len(output) > 0, "visualize did not produce any output.")

if __name__ == '__main__':
    unittest.main()
