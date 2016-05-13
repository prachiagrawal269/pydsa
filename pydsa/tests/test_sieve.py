from pydsa.sieve import sieve


def test_sieve():
    Primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    assert sieve(50) == Primes
