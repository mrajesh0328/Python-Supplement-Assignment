# Problem 63: Find longest word in a sentence
# Find and fix the error

def find_longest_word(sentence):
    words = sentence.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

text = "The quick fox jumps"
print(f"Longest word: {find_longest_word(text)}")
