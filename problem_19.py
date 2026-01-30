# Problem 19: Calculate power of a number
# Find and fix the error

def power(base, exponent):
    result = 1
    for i in range(exponent):
        result *= base
    return result

print(f"2^7 = {power(2, 7)}")
