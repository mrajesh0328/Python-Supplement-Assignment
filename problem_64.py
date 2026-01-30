# Problem 64: Merge two sorted lists
# Find and fix the error

def merge_sorted(list1, list2):
    merged = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged

l1 = [1, 3, 5]
l2 = [2, 4, 6]
print(f"Merged: {merge_sorted(l1, l2)}")

