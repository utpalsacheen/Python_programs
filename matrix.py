def matrixSum(matrix):
    sum = 0
    pr = set()
    print("set: ")
    print(pr)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                pr.add((i+1, j))
            else:
                if (i,j) not in pr:
                    sum = sum + matrix[i][j]
                else:
                    pr.add((i+1, j))

    print(pr)
    print("sum: " + str(sum))
    return sum

matrix = [[0,1,1,2], [0,5,0,0], [2,0,3,3]]
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))
assert matrixSum(matrix) == 9, "Sum of the matrix is not 9"

matrix1 = [[1,1,1,0], [0,5,0,1], [2,1,3,10]]
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix1]))
assert matrixSum(matrix1) == 9, "Sum of the matrix is not 9"

matrix2 = [[1,1,1], [2,2,2], [3,3,3]] 
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix2]))
assert matrixSum(matrix2) == 18, "Sum of the matrix is not 18"

matrix3 = [[0]] 
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix3]))
assert matrixSum(matrix3) == 0, "Sum of the matrix is not 0"
