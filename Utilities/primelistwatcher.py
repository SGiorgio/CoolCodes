import requests
import xml.etree.ElementTree as ET
import numpy as np

global loc
loc = 0

def generate_primes(n=100):
    """Generate the first n prime numbers."""
    primes = []
    candidate = 2
    while len(primes) < n:
        is_prime = all(candidate % p != 0 for p in primes)
        if is_prime:
            primes.append(candidate)
        candidate += 1
    return primes

def Pn(n):
    P = generate_primes(n)
    Prod = 1
    for i in range(n):  # Fix indexing to iterate correctly
        Prod *= P[i]
    return Prod

# Binary search is an efficient algorithm for finding an item in a sorted list.
# It works by repeatedly dividing the search interval in half.
# If the target value is less than the middle element, search the left half.
# Otherwise, search the right half. This process continues until the value is found or the interval is empty.

def is_prime(n, p):
    """Checks if a number is prime by looking in the sieve."""
    global loc  # Use the global loc variable
    for i in range(loc, len(p)):  # Start searching from loc
        if p[n]:
            return True
        else:
            return False


def sieve_of_eratosthenes(limit):
    """Generate prime numbers up to 'limit' using a bit array and ignoring even numbers."""
    if limit < 2:
        return []

    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for start in range(2, int(limit**0.5) + 1):
        if sieve[start]:
            for multiple in range(start * start, limit + 1, start):
                sieve[multiple] = False

    primes = [num for num, is_prime in enumerate(sieve) if is_prime]
    return primes

def sieve_of_eratosthenes_optimized(limit):
    sieve = np.ones(limit // 2, dtype=bool)  # Only store odd numbers
    sieve[0] = False  # 1 is not prime
    for i in range(1, int(limit**0.5) // 2 + 1):
        if sieve[i]:
            start = 2 * i * (i + 1)
            sieve[start::2 * i + 1] = False
    primes = [2] + [2 * i + 1 for i in range(len(sieve)) if sieve[i]]
    return primes

def sieve_memory_usage(limit):
    """Calculate the memory usage of the Sieve of Eratosthenes."""
    memory_usage = (limit + 1)  # Each boolean value is 1 byte
    print(f"Memory usage for sieve with limit {limit}: {memory_usage / (1024**2):.2f} MB")

# Example usage:
sieve_memory_usage(10**9)

##The idea is to count weak, strong and non prime numbers in a n range

##Eratosthenes compilation 
P = sieve_of_eratosthenes(10**9)
n = 6
a = 2
strg = 0
weak = 0
nonp = 0
exit()
if P[-1] >= n**(2 * n):  # Corrected indexing for the last element
    print("e va buon dai")
else:
    print("no bono")
    exit()  # Stop the program execution


Pn_value = Pn(n)  # Precompute Pn(n) once
for a in range(1, (n**n) + 1):  # Start from 1 to avoid redundant checks
    gn1 = (Pn_value * a) + 1
    gn2 = gn1 - 2

    gn2_is_prime = is_prime(gn2, P)  # Check gn1 once
    gn1_is_prime = is_prime(gn1, P)  # Check gn2 once

    if gn1_is_prime and gn2_is_prime:
        strg += 1
        print(a, "\t | STRONG | ", gn1, gn2)
    elif gn1_is_prime ^ gn2_is_prime:
        weak += 1
        print(a, "\t |  WEAK  | ", gn1 if gn1_is_prime else gn2)
    else:
        nonp += 1
        print(a, "\t |  NONPR | ")

print(f"For the given n value there are ",strg," strong coefficients,",weak," weak coefficients, and ",nonp," non-primes.")

## n = 3 -- % of primes 92,30%
## n = 4 -- % of primes 72,70%
## n = 5 -- % of primes 54,00%
## n = 6 -- % of primes 83,97%
## n = 7 -- % of primes