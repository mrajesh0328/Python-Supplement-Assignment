# Problem 14: Check if a number is prime
# Find and fix the error

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number% i == 0:
            return False
    return True

print(f"Is 17 prime? {is_prime(17)}")
