"""Module to generate and check prime numbers, albeit in a naive way"""

import math
import random
import secrets

def is_prime_trial_div(num):
    """
        Returns True if num is a primve number, otherwise false
    """
    # All numbers less than two are not prime
    if num < 2:
        return False

    # Determine if num is divisible by any number up to sqrt of num
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def prime_sieve(sieve_size):
    """
        Returns a list of prime numbers calculated using the Sieve
        of Eratosthenes algorithm.
    """
    sieve = [True] * sieve_size
    sieve[0] = False
    sieve[1] = False 

    for i in range(2, int(math.sqrt(sieve_size)) + 1):
        pointer = i * 2
        while pointer < sieve_size:
            sieve[pointer] = False
            pointer += i

    # Compile list of primes
    primes = []
    for i in range(sieve_size):
        if sieve[i] == True:
            primes.append(i)

    return primes


def rabin_miller(num):
    """Rabin-Miller Algorithm"""
    if num % 2 == 0 or num < 2:
        return False
    