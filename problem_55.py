# Problem 55: Count frequency of each element
# Find and fix the error

def count_frequency(lst):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(f"Frequency: {count_frequency(numbers)}")

