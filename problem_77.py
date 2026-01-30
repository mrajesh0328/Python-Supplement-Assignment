# Problem 77: Check if number is perfect square
# Find and fix the error

def is_perfect_square(n):
    sqrt = n ** 0.5
    return sqrt == int(sqrt)

print(f"Is 16 perfect square? {is_perfect_square(16)}")
print(f"Is 9 perfect square? {is_perfect_square(9)}")
