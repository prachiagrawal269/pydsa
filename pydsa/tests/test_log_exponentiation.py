from pydsa.logarithmic_exponentiation import *
from random import randint


def test_logarithmic_exponentiation():
    a = randint(1, 100)
    b = randint(1, 100)

    assert logarithmic_exponentiation(a, b) == (a)**(b)
