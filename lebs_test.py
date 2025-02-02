import random
import numpy as np
import pytest
from collections import Counter, defaultdict

# Import your functions. Replace 'my_module' with the actual module name.
from lebs import (
    singlepattern,
    globalpattern,
    overview,
    parsesectors,
    learner
)

# --- Test for singlepattern ---
def test_singlepattern():
    # Create a small sample array and define objectives.
    sample_array = np.array([
        [1, 2, 3],
        [4, 1, 6],
        [3, 5, 1]
    ])
    objectives = [1, 3, 6]
    pattern_y, pattern_x = singlepattern(sample_array, objectives)
    
    # For each coordinate, verify the element is one of the objectives.
    for y, x in zip(pattern_y, pattern_x):
        assert sample_array[y][x] in objectives, f"Element at ({y},{x}) not in objectives"



# --- Test for overview ---
def test_overview():
    # Create a list of match dictionaries similar to what parsesectors returns.
    matches = [
        {'value': 1, 'sector': 0, 'position': (0, 0)},
        {'value': 3, 'sector': 0, 'position': (1, 1)},
        {'value': 6, 'sector': 1, 'position': (0, 0)},
        {'value': 1, 'sector': 1, 'position': (1, 1)},
        {'value': 1, 'sector': 1, 'position': (2, 2)},
    ]
    summary = overview(matches)
    # Expected counts:
    # Sector 0: 1 occurrence of 1 and 1 of 3.
    # Sector 1: 1 occurrence of 6 and 2 of 1.
    assert summary[0][1] == 1, "Sector 0 should have 1 occurrence of value 1"
    assert summary[0][3] == 1, "Sector 0 should have 1 occurrence of value 3"
    assert summary[1][6] == 1, "Sector 1 should have 1 occurrence of value 6"
    assert summary[1][1] == 2, "Sector 1 should have 2 occurrences of value 1"

# --- Test for parsesectors in non-brutal mode ---
def test_parsesectors_non_brutal():
    # Use a small 6x6 matrix that divides evenly into 3x3 sectors.
    data = [
        [1, 2, 3, 4, 5, 6],
        [7, 1, 2, 3, 6, 2],
        [6, 5, 1, 3, 3, 4],
        [3, 4, 6, 1, 2, 7],
        [1, 2, 3, 4, 6, 5],
        [7, 8, 9, 1, 2, 3]
    ]
    objectives = [1, 3, 6]
    # Use sector size (3,3) and non-brutal mode.
    matches = parsesectors(data, objectives, vector=(3, 3), brutal=False)
    # Check that matches is a list and that each match's value is in objectives.
    assert isinstance(matches, list)
    for match in matches:
        assert match['value'] in objectives, f"Value {match['value']} not in objectives"

# --- Test for parsesectors in brutal mode ---
def test_parsesectors_brutal():
    # Use the same small 6x6 matrix.
    data = [
        [1, 2, 3, 4, 5, 6],
        [7, 1, 2, 3, 6, 2],
        [6, 5, 1, 3, 3, 4],
        [3, 4, 6, 1, 2, 7],
        [1, 2, 3, 4, 6, 5],
        [7, 8, 9, 1, 2, 3]
    ]
    objectives = [1, 3, 6]
    # Use brutal mode.
    matches = parsesectors(data, objectives, vector=(3, 3), brutal=True)
    # Check that matches is a list and that each match's value is in objectives.
    assert isinstance(matches, list)
    for match in matches:
        assert match['value'] in objectives, f"Value {match['value']} not in objectives"

# --- Test for learner ---
def test_learner(capsys):
    # Use a small 4x4 matrix that divides evenly into 2x2 sectors.
    data = [
        [1, 2, 3, 4],
        [3, 1, 6, 2],
        [6, 5, 1, 3],
        [3, 4, 6, 1]
    ]
    objectives = [1, 3, 6]
    # Call learner in brutal mode to process every element.
    results = learner(data, objectives, vector=(2, 2), brutal=True)
    # Verify that results is a list.
    assert isinstance(results, list)
    for match in results:
        assert match['value'] in objectives, f"Value {match['value']} not in objectives"
    
    # Check printed output for sector info.
    captured = capsys.readouterr().out
    assert "In sector" in captured, "Printed output should include sector information"
