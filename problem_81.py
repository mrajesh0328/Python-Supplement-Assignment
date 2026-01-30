# Problem 81: Check if string has balanced brackets
# Find and fix the error

def balanced_brackets(s):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in s:
        if char in pairs:
            stack.append(char)
        elif char in pairs.values():
            if not stack or pairs[stack.pop()] != char:
                return False
    return len(stack) == 0

expr = "{[()]}"
print(f"Balanced: {balanced_brackets(expr)}")

