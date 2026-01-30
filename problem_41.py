# Problem 41: Find index of element in list
# Find and fix the error

numbers = [10, 20, 30, 40, 50]
search = 20
index = -1
for i in range(len(numbers)):
    if numbers[i] == search:
        index = i
print(f"Index of {search}: {index}")
