# Logarithmic exponentiation
# Logarithmic Exponentiation
# Complexity: O(log(exponent))

# Reference used:
# https://discuss.codechef.com/questions/20451/a-tutorial-on-fast-modulo-multiplication-exponential-squaring


def log_exp(base, exponent):

    """
        Performs logarithmic exponentiation in log(exponent) time.

    Basic Idea: (a^b) : ((a^2)^(b/2)) if b is even
                 a*((a^2)^((b-1)/2))  if b is odd
                 1                    if b is 0


    >>> from pydsa import log_exp
    >>> a = 10
    >>> b = 2
    >>> log_exp(a, b)
    100

    """

    result = 1

    while (exponent > 0):

        if (exponent % 2 == 1):   # exponent is odd since "1" at one's place
            result = result*base

        base = base*base
        exponent = exponent//2

    return result
