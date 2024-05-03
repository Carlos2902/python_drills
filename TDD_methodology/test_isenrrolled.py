import Enrolled
from curses.ascii import isdigit




def test_ispresent():
    assert Enrolled.ispresent("Al")
def test_nondigit():
    assert Enrolled.nondigit("NN")