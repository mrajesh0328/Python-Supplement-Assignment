# Problem 97: Remove element from list
# Find and fix the error

def remove_element(nums, val):
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i

numbers = [3, 2, 2, 3, 4, 6]
length = remove_element(numbers, 3)
print(f"New length: {length}")
print(f"Modified list: {numbers[:length]}")
