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
    # Doesn't work on even integers
    if num % 2 == 0 or num < 2:
        return False
    if num == 3:
        return True
    
    s = num - 1
    t = 0

    while s % 2 == 0:
        # Keep halving s until it is odd (and use t to 
        # count how many times we halve)
        s = s // 2
        t += 1
    for trials in range(5):
        # Try to falsify num's primality 5 times.
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True

LOW_PRIMES = prime_sieve(100)

def is_prime(num):
    """
        Return True if num is a prime number. This function does a quicker prime
        number chekc before calling rabin_miller()
    """
    if num < 2:
        return False
    
    # See if any of the low prime numbers can divide num
    for prime in LOW_PRIMES:
        if (num % prime == 0):
            return False

    # If all else fails, call rabin_miller() to determine if num is prime
    return rabin_miller(num)


def generate_large_prime_number(keysize=1024):
    """Return a large prime number that is keysize bits in size"""
    while True:
        num = random.randrange(2**(keysize - 1), 2**(keysize))
        if is_prime(num):
            return num