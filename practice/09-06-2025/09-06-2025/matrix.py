def diagonal_sum(matrix):
    n = len(matrix)
    total = 0

    for i in range(n):
        total += matrix[i][i]              
        total += matrix[i][n - 1 - i]     
    if n % 2 == 1:
        total -= matrix[n // 2][n // 2]

    return total


matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
result = diagonal_sum(matrix)
print("Sum of primary and secondary diagonals:", result)