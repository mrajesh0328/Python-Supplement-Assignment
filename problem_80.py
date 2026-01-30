# Problem 80: Find mode (most frequent element)
# Find and fix the error

def find_mode(lst):
    freq = {}
    for item in lst:
        freq[item] = freq.get(item, 0) + 1
    
    max_freq = max(freq.values())
    for key, value in freq.items():
        if value == max_freq:
            return key

numbers = [1, 2, 2, 3, 3, 3, 5]
print(f"Mode: {find_mode(numbers)}")
