# Problem 32: Find minimum in a list
# Find and fix the error

numbers = [45, 12, 78, 34, 9]
minimum = numbers[0]
for num in numbers:
    if num < minimum:
        minimum = num
print(f"Minimum: {minimum}")
