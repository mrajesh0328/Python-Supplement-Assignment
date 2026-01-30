# Problem 94: Count bits set to 1
# Find and fix the error

def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n = n >> 1
    return count

print(f"Set bits in 15: {count_set_bits(15)}")

