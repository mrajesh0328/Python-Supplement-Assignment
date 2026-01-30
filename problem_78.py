# Problem 78: Find duplicate elements in list
# Find and fix the error

def find_duplicates(lst):
    seen = set()
    duplicates = []
    for item in lst:
        if item in seen:
            duplicates.append(item)
        seen.add(item)
    return duplicates

numbers = [1, 2, 3, 2, 6, 3, 5]
print(f"Duplicates: {find_duplicates(numbers)}")
