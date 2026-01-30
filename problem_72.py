# Problem 72: Count uppercase and lowercase letters
# Find and fix the error

def count_case(text):
    upper = 0
    lower = 0
    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    return upper, lower

sentence = "Hello world"
u, l = count_case(sentence)
print(f"Uppercase: {u}, Lowercase: {l}")
