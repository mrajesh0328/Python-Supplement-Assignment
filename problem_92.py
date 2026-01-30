# Problem 92: Check if all elements are unique
# Find and fix the error

def all_unique(lst):
    return len(lst) == len(set(lst))

numbers = [1, 2, 3, 4, 5]
print(f"All unique: {all_unique(numbers)}")

