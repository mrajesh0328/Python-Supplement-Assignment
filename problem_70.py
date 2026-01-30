# Problem 70: Find all prime numbers up to n
# Find and fix the error

def find_primes(n):
    primes = []
    if n < 2:
        return primes
    for num in range(2, n + 1):
        is_prime = True
        i = 2
        # only test divisors up to sqrt(num)
        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            primes.append(num)
    return primes

print(f"Primes up to 20: {find_primes(20)}")
