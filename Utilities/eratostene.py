def sieve_of_eratosthenes(limit):
    # Create a boolean array "prime[0..limit]" and initialize all entries as True
    prime = [True] * (limit + 1)
    p = 2

    while p * p <= limit:
        if prime[p]:
            # Marking multiples of p as False
            for i in range(p * p, limit + 1, p):
                prime[i] = False
        p += 1

    # Collecting all prime numbers
    primes = [p for p in range(2, limit + 1) if prime[p]]
    return primes


if __name__ == "__main__":
    limit = 10**9
    print("Calculating primes up to", limit)
    primes = sieve_of_eratosthenes(limit)
    print("Number of primes found:", len(primes))