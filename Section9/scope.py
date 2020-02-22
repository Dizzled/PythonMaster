def fact(n):
    """ Calculate n! iteratively """
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result

def factorial(n):
    # n! can also be defined as n * (n - 1)!
    """ calculates n! recursively"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def fib(a, b):
    """ F(n) = F(n - 1) + F(n - 2)"""
    if a < 2:
        return a
    else:
        return fib(a - 1) + fib(b - 2)


def fibonacci(n):
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        nMinus1 = 1
        nMinus2 = 0
        for f in range(1, n):
            result = nMinus1 + nMinus2
            nMinus2 = nMinus1
            nMinus1 = result

    return result


