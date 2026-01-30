# Problem 96: Find two numbers that sum to target
# Find and fix the error

def two_sum(nums, target):
    seen = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in seen:
            return [seen[complement], i]
        seen[nums[i]] = i
    return []

numbers = [2, 7, 11, 16]
print(f"Indices: {two_sum(numbers, 9)}")
