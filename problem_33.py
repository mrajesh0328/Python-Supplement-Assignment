# Problem 33: Check if string contains only digits
# Find and fix the error

def is_all_digits(text):
    for char in text:
        if not char.isdigit():
            return False
    return True

test_str = "2345"
print(f"Is all digits: {is_all_digits(test_str)}")
