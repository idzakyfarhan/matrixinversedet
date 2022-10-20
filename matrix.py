





def main():
    while True:

        print("  Linear Algebra  ")

        # Exit if matrix is empty
        while True:
            rows = int(input("Number of Rows : "))
            if rows < 1:
                print("Matrix cannot be empty")
            else: break


        print("Input the elements of the matrix on each row")
        matrix = create_matrix(rows)

        # Check whether it's a square matrix
        if not is_square_matrix(matrix):
            print("Matrix is not a square matrix and therefore")
            print("has no determinant and inverse. However,")
            print("a pseudo-inverse may exist")
        else:

            print("\n    RESULT    ")
            print("Your matrix: ")
            print_matrix(matrix)

            det = determinant(matrix)
            print(f"Determinant: {det}")

        # Exit when it has no inverse
            if det == 0:
                print("Determinant of 0 means the matrix has no inverse")

            if det != 0:

                print("Inverse:")
                inversed = inverse(matrix)
                print_matrix(inversed)

        finish = input("Continue or finish? ")
        # while True :
        if finish == "finish":
            break


def print_matrix(matrix):
    # for each element in the matrix
    # pad with 6 spaces and a precision of 2 digits after decimal point
    print("\n".join(["".join([f"{v:8.2f}"for v in row]) for row in matrix]))


def create_matrix(rows):
    matrix = []

    for i in range(rows):
        elems = input(f"Row {i + 1}: ")
        # Split string to get individual element,
        # then convert each element to integer and lastly,
        # append to matrix
        matrix.append([float(v) for v in elems.split()])

    return matrix


def is_square_matrix(matrix):
    rows = len(matrix)
    for _, row in enumerate(matrix):
        if rows != len(row):
            return False
    return True


def minor(matrix, pv_row, pv_col):
    minor_matrix = []

    for i, rows in enumerate(matrix):
        temp = []
        for j, elem in enumerate(rows):
            if i != pv_row and j != pv_col:
                temp.append(elem)
        if len(temp) != 0:
            minor_matrix.append(temp)

    return minor_matrix


def transpose(matrix):
    transposed = []

    for i in range(len(matrix[0])):
        col = []
        for cols in matrix:
            col.append(cols[i])
        transposed.append(col)

    return transposed


def determinant(matrix, pivot=0):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    else:
        det = 0
        i = pivot
        for j in range(len(matrix)):
            cofactor = (-1)**(i + j) * matrix[i][j] * determinant(
                minor(matrix, i, j))
            det += cofactor

    return det


def inverse(matrix):
    # Build the determinant matrix
    determinant_matrix = []

    for i, rows in enumerate(matrix):
        temp = []
        for j, _ in enumerate(rows):
            temp.append(determinant(minor(matrix, i, j)))
        determinant_matrix.append(temp)

    # Next, transpose the determinant matrix, reapply cofactor,
    # then multiply by 1/det
    inverted = transpose(determinant_matrix)
    det = determinant(matrix)

    for i, rows in enumerate(inverted):
        for j, elem in enumerate(rows):
            inverted[i][j] = (-1)**(i + j) * elem * (1.0 / det)

    return inverted


if __name__ == "__main__":
    main()