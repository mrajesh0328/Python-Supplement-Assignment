# Problem 99: Find maximum subarray sum
# Find and fix the error

def max_subarray_sum(arr):
    if not arr: 
        return 0
    max_sum = arr[0]
    current_sum = arr[0]
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    return max_sum
numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"Maximum subarray sum: {max_subarray_sum(numbers)}")
