# Problem 89: Check if number is palindrome
# Find and fix the error

def is_palindrome_number(n):
    original = n
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
    return original == reversed_num

print(f"Is 121 palindrome? {is_palindrome_number(121)}")

