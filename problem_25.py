# Problem 25: Find GCD of two numbers
# Find and fix the error

def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

print(f"GCD of 20 and 8: {gcd(20,8)}")
