import random

matrix_1 = [[random.randint(-50, 50) for _ in range(10)] for _ in range(10)]
matrix_2 = [[random.randint(-50, 50) for _ in range(10)] for _ in range(10)]

def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
            result.append(row)
            return result

matrix_3 = add_matrices(matrix_1, matrix_2)

print("Матрица 1:")
for row in matrix_1:
    print(row)

print("\nМатрица 2:")
for row in matrix_2:
    print(row)

print("\nРезультирующая матрица:")
for row in matrix_3:
    print(row)
