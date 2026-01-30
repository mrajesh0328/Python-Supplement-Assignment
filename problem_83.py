# Problem 83: Find kth smallest element
# Find and fix the error

def kth_smallest(arr, k):
    sorted_arr = sorted(arr)
    return sorted_arr[k-1]

numbers = [7, 10, 4, 3, 20, 15]
print(f"3rd smallest: {kth_smallest(numbers, 3)}")
