# Problem 61: Find pairs with given sum
# Find and fix the error

def find_pairs(arr, target):
    pairs = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
    return pairs

numbers = [1, 2, 3, 4, 5]
print(f"Pairs with sum 5: {find_pairs(numbers, 5)}")
