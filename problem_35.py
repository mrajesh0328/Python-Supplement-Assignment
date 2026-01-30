# Problem 35: Calculate percentage
# Find and fix the error

def calculate_percentage(obtained, total):
    percentage = (obtained / total) * 100
    return percentage

marks = 46
total_marks = 50
result = calculate_percentage(marks, total_marks)
print(f"Percentage: {result}%")
