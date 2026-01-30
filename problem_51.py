# Problem 51: Reverse words in a sentence
# Find and fix the error

def reverse_words(sentence):
    words = sentence.split()
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
    return " ".join(reversed_words)

text = "Hello World"
print(f"Reversed words: {reverse_words(text)}")

