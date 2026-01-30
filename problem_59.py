# Problem 59: Rotate list by k positions
# Find and fix the error

def rotate_list(lst, k):
    n = len(lst)
    k = k % n
    return lst[k:] + lst[:k]

numbers = [1, 2, 3, 4, 5]
print(f"Rotated by 2: {rotate_list(numbers, 2)}")

