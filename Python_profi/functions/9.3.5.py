def print_operation_table(operation, rows, cols):
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = operation(i+1, j+1)
    for line in matrix:
        print(*line)


print_operation_table(lambda a, b: a * b, 5, 5)
print_operation_table(pow, 5, 4)

# with map
# def print_operation_table(operation, rows, cols):
#     for i in range(1, rows + 1):
#         print(*map(operation, [i] * cols, range(1, cols + 1)))
