# Problem 67: Remove nth element from list
# Find and fix the error

def remove_nth(lst, n):
    if n >= 0 and n < len(lst):
        return lst[:n] + lst[n+1:]
    return lst

numbers = [1, 2, 3, 4, 6]
result = remove_nth(numbers, 2)
print(f"After removing: {result}")
