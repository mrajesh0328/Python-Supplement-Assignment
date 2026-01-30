# Problem 56: Remove vowels from string
# Find and fix the error

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result

sentence = "Hello World"
print(f"Without vowels: {remove_vowels(sentence)}")

