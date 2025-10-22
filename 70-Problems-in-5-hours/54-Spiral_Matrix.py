def spiralOrder(matrix: List[List[int]]) -> List[int]:
    #INPUT: m x n matrix
    #OUTPUT: return matrix in a spiral order

    spiral_matrix = []

    while matrix:

        # Add the the first row of the matrix
        spiral_matrix += (matrix.pop(0))

        # Add the last element of all rows in order 
        if matrix and matrix[0]:
            for row in matrix:
                spiral_matrix.append(row.pop())

        # Add the reverse of last row 
        if matrix:
            spiral_matrix += (matrix.pop()[::-1])

        # Add the first element in each row in reverse
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                spiral_matrix.append(row.pop(0))

        return spiral_matrix

