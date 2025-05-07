def rotate_matrix(matrix: list[list[int]]) -> None:
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()

# Example usage
if __name__ == "__main__":
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    rotate_matrix(mat)
    print(mat)
    # Output: [
    #  [7, 4, 1],
    #  [8, 5, 2],
    #  [9, 6, 3]
    # ]
