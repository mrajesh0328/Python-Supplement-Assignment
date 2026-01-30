# Problem 91: Implement selection sort
# Find and fix the error

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

numbers = [64, 25, 13, 22, 11]
print(f"Sorted: {selection_sort(numbers)}")
