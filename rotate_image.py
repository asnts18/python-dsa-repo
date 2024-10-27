"""
    Abegail Santos
    Date: 10/24/24
"""

def rotate_90_deg(matrix):
    """
    A function to rotate an n x n 2D matrix 
    representing an image by 90 degrees clockwise. 
    Rotation is done in-place.
    """
    n = len(matrix)
    
    # transpose
    for i in range(n):
        for j in range(i, n): 
            matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
            
    # flip or swap
    for i in range(n):
        for j in range(n//2):
            matrix[i][j], matrix[i][n - j - 1] =  matrix[i][n - j - 1], matrix[i][j]
    
    return matrix

def print_matrix(matrix):
    """
    Function: print out matrix
    """
    for row in matrix:
        print(' '.join(map(str, row)))

def main():
    matrix_a = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    
    rotated_matrix = rotate_90_deg(matrix_a)
    print_matrix(rotated_matrix)    
    
if __name__ == "__main__":
    main()
