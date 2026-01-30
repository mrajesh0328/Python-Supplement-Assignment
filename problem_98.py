# Problem 98: Check if power of two
# Find and fix the error

def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

print(f"Is 16 power of 2? {is_power_of_two(16)}")
print(f"Is 20 power of 2? {is_power_of_two(20)}")
