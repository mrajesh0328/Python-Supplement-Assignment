# Problem 86: Find sum of matrix diagonals
# Find and fix the error

def diagonal_sum(matrix):
    n = len(matrix)
    total = 0
    for i in range(n):
        total += matrix[i][i]
        total += matrix[i][n-1-i]
    return total

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Diagonal sum: {diagonal_sum(mat)}")

