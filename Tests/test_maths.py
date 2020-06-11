import pytest
from Code.maths import isPrime

def test_isPrime():
    assert isPrime(5) == True
    assert isPrime(8) == False