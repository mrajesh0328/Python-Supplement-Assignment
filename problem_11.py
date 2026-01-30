# Problem 11: Count occurrences of each character
# Find and fix the error

character = "programming"
char_count = {}
for char in character:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)
