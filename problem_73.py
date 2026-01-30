# Problem 73: Find maximum difference between elements
# Find and fix the error

def max_difference(arr):
    if len(arr) < 2:
        return 0
    min_val = arr[0]
    max_diff = 0
    for i in range(1, len(arr)):
        if arr[i] - min_val > max_diff:
            max_diff = arr[i] - min_val
        if arr[i] < min_val:
            min_val = arr[i]
    return max_diff

numbers = [7, 1, 5, 3, 8, 4]
print(f"Max difference: {max_difference(numbers)}")
