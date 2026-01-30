# Problem 40: Count consonants in a string
# Find and fix the error

def count_consonants(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

sentence = "Hello "
print(f"Number of consonants: {count_consonants(sentence)}")
