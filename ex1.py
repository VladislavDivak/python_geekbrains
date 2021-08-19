class Matrix:
    def __init__(self, lines, columns, args):
        self.lines = int(lines)
        self.columns = int(columns)
        self.matrix = list(args)

    def __str__(self):
        matrix_show = []
        start = 0
        for i in range(1, len(self.matrix)+1):
            if i % self.columns == 0:
                matrix_show.append(' '.join(map(str, self.matrix[start:i])))
                start += self.columns
        matrix_show = "\n".join(map(str, matrix_show))
        return f'{matrix_show}'

    def __add__(self, other):
        new_matrix = []
        for i in range(len(self.matrix)):
            new_matrix.append(self.matrix[i] + other.matrix[i])
        add_matrix = Matrix(self.lines, self.columns, new_matrix)
        return print(add_matrix)


matrix1 = Matrix(3, 2, [1, 2, 3, 4, 5, 6])
matrix2 = Matrix(2, 3, [9, 8, 7, 6, 5, 4])

print(matrix1)
print(matrix2)
print(matrix1 + matrix2)
