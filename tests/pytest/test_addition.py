import addition
import pytest

def test_add():
    assert addition.add(4,9) == 13
def test_sub():
    assert addition.sub(4,9) == -5