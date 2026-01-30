# Problem 90: Find median of a list
# Find and fix the error

def find_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 0:
        median = (sorted_lst[n//2] + sorted_lst[n//2 - 1]) / 2
    else:
        median = sorted_lst[n//2]
    return median

numbers = [1, 3, 5, 7, 11]
print(f"Median: {find_median(numbers)}")
