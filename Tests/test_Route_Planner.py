import pytest 
from Code.Route_Planner import * 

def test_FindHighestNum():
    assert FindHighestNum([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 15
def test_FindLowestPeak():
    assert FindLowestPeak([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 0, 15) == 2
def test_RoutePlanner():
    assert RoutePlanner([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 15) == [0, 2, 6, 9, 11, 15]