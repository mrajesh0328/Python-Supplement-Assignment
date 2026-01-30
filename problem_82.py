# Problem 82: Remove adjacent duplicates
# Find and fix the error

def remove_adjacent_duplicates(text):
    result = []
    for char in text:
        if len(result) == 0 or result[-1] != char:
            result.append(char)
    return "".join(result)

s = "Python programming"
print(f"After removal: {remove_adjacent_duplicates(s)}")
