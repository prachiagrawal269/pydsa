# Sieve of Eratosthenes
# Referred link - http://www.geeksforgeeks.org/sieve-of-eratosthenes/


def sieve(limit):

    """
    Print all the prime numbers smaller than or equal to the given number
    >>> from pydsa.sieve import sieve
    >>> sieve(10)
    [2, 3, 5, 7]
    """

    lim = limit + 1
    not_prime = [False]*lim
    primes = []
    not_prime[0] = True
    not_prime[1] = True

    for i in range(2, lim):
        if not_prime[i]:
            continue
        for f in range(i*2, lim, i):
            not_prime[f] = True

        primes.append(i)

    return primes
