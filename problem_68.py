# Problem 68: Find sum of even indexed elements
# Find and fix the error

def sum_even_indices(lst):
    total = 0
    for i in range(0, len(lst), 2):
        total += lst[i]
    return total

numbers = [1, 2, 3, 4, 5, 6]
print(f"Sum of even indices: {sum_even_indices(numbers)}")

