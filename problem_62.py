# Problem 62: Convert decimal to binary
# Find and fix the error

def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

print(f"Binary of 10: {decimal_to_binary(10)}")
