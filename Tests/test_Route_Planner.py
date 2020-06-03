import pytest 
from Code.Route_Planner import * 

def test_FindHighestNum():
    assert FindHighestNum([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 15
def test_RoutePlanner():
    assert RoutePlanner([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 15) == [8, 12, 14, 15]