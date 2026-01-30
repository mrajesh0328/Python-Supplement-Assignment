# Problem 47: Check if string starts with a specific character
# Find and fix the error

def starts_with(text, char):
    if text and text[0] == char:
        return True
    return False

word = "Python"
print(f"Starts with 'P': {starts_with(word, 'P')}")
print(f"Starts with 'J': {starts_with('', 'J')}")
