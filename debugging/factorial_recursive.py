#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
        Calculates the factorial of a given non-negative integer using recursion.

    Parameters:
        n (int): A non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial value of the input number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Komanda sətrindən arqumenti oxuyuruq və faktorialı hesablayırıq
f = factorial(int(sys.argv[1]))
print(f)
