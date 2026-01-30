# Problem 24: Remove all spaces from a string
# Find and fix the error

text = "Hello From Python"
no_spaces = ""
for char in text:
    if char != " ":
        no_spaces += char
print(f"Without spaces: {no_spaces}")
