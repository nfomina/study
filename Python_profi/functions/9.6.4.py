def matrix_to_dict(matrix: list[list[int | float]]) -> dict[int, list[int | float]]:
    return{i: matrix[i-1] for i in range(1, len(matrix)+1)}


# TEST_1:
matrix = [[5, 6, 7], [8, 3, 2], [4, 9, 8]]

print(matrix_to_dict(matrix))

# TEST_2:
matrix = [[5.1, 6, 7.94]]

print(matrix_to_dict(matrix))

# TEST_3:
annotations = matrix_to_dict.__annotations__

print(annotations['return'])

# TEST_4:
matrix = [[3, 66, 71], [8.0, 3.1, 2.88], [13, 22, 76], [19, 21, 22]]

print(matrix_to_dict(matrix))

# TEST_5:
print(*matrix_to_dict.__annotations__.values())

# TEST_6:
matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]

print(matrix_to_dict(matrix))

# TEST_7:
matrix = [[1, 2, 3, 4, 5, 6, 7, 8]]

print(matrix_to_dict(matrix))
