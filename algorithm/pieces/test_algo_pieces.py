import pytest
from algo_pieces import *

def test_targets():
    targets = 2
    expected = 0.75
    actual = target_num(targets)
    assert expected == actual