# Problem 50: Convert string to uppercase
# Find and fix the error

text = "python programming"
uppercase = ""
for char in text:
    if char >= 'a' and char <= 'z':
        uppercase += chr(ord(char) - 32)
    else:
        uppercase += char
print(f"Uppercase: {uppercase}")

