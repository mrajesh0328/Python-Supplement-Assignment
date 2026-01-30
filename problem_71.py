# Problem 71: Transpose a matrix
# Find and fix the error

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        result.append(row)
    return result

mat = [[1, 2, 3], [4, 5, 6]]
print(f"Transposed: {transpose(mat)}")

