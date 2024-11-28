def get_matrix (n, m, value):
    matrix = []
    for i in range(n):
        line = []
        matrix.append(line)
        for j in range(m):
            line.append(value)
    return matrix
result1 = get_matrix(5, 3, 27)
result2 = get_matrix(4, 2, 36)
result3 = get_matrix(7, 4, 7)

print(result1)
print(result2)
print(result3)

