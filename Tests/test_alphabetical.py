import pytest
from Code import Alphabetical

def test_sorter():
    assert Alphabetical.sorter("without,hello,bag,world")=="bag,hello,without,world"