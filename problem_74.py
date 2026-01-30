# Problem 74: Find first non-repeating character
# Find and fix the error

def first_non_repeating(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for char in text:
        if char_count[char] == 1:
            return char
    return None

word = "programming"
print(f"First non-repeating: {first_non_repeating(word)}")
