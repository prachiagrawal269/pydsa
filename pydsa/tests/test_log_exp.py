from pydsa.log_exp import *
from random import randint


def test_log_exp():
    a = randint(1, 50)
    b = randint(1, 50)

    assert log_exp(a, b) == (a)**(b)
