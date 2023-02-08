import numpy as np
def print_matrix(matrix):

    for i in range(len(matrix)):
        temp = ''
        for j in range(len(matrix[0])):
            temp += f"{matrix[i][j]} "
        print(f"{temp}\n")

def get_new_matrix(r, c, matrix):
    new_matrix = []
    row_slice = matrix[:r] + matrix[r+1:]
    for row in row_slice:
        new_matrix.append(row[:c] + row[c+1:])
    return new_matrix

def calc_det_matrix_base(matrix):
    # Function for calculating 2x2 matrix derivative
    return matrix[0][0]*matrix[1][1] - matrix[0][1] * matrix[1][0]

def calc_det_matrix(matrix):
    if len(matrix) == 2:
        return calc_det_matrix_base(matrix)

    det = 0
    for c in range(len(matrix[0])):
        sign = matrix[0][c] if c%2 == 0 else -matrix[0][c]
        det += sign * calc_det_matrix(get_new_matrix(0, c, matrix))

    return det

def main():
    a = [[1, 2, 3, 10], [-1, 2, 3, 4], [5, 6, 2, 0], [1, 6, 8, 4]]
    #get_new_matrix(1, 1, a)
    b = calc_det_matrix(a)
    npDet = np.linalg.det(a)
    print(f"Numpy deteriminant: {npDet}")
    print(f"Calculated deterimnant: {b}")
main()
