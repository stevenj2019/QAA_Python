import pytest
from Code.Integral_Dictionary import IntegralDictionary

def test_Integral_Dictionary():
    assert IntegralDictionary(3) == {1:1, 2:4, 3:9}