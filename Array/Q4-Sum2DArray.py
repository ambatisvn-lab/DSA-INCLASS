
'''
As we have understood 2D arrays, let's implement a function that computes the sum of all elements in a 2D array.

input: A 2D array (list of lists) of integers.
output: The sum of all elements in the 2D array (integer).
'''
def add_matrices(arr1, arr2, res):
    """
    Add two matrices arr1 and arr2 and store the result in res (in-place).
    Assumes arr1, arr2, res are lists of lists with the same dimensions.
    """
    rows = len(arr1)
    cols = len(arr1[0]) if rows else 0
    for i in range(rows):
        for j in range(cols):
            res[i][j] = arr1[i][j] + arr2[i][j]
    return res

#Driven code
if __name__ == "__main__":
    # Example usage:
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matrix2 = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    summed_matrix = add_matrices(matrix1, matrix2, result)
    print("Summed Matrix:")
    for row in summed_matrix:
        print(row)


