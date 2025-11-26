
'''
Matrix Diagonal Sum
Given a square matrix mat, return the sum of the matrix diagonals. Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.
Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
Example 2:
Input: mat = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
Output: 8

Approach 1: Brute Force
We can iterate through each element of the matrix and check if it lies on either of the diagonals. If it does, we add it to our total sum. This approach has a time complexity of O(n^2) since we are iterating through all elements of the n x n matrix.
"clear approach is in book".indices are important here (0,0),(1,1),(2,2)... for primary and (0,n-1),(1,n-2),(2,n-3)... for secondary
'''
def diagonal_sumB(mat):
    n = len(mat)
    total = 0
    for i in range(n): #both loops run n times
        for j in range(n):
            if i==j or i+j==n-1: #primary and secondary diagonal condition
                total += mat[i][j]
    return total

def diagonal_sumO(mat):
    n = len(mat)
    total = 0
    for i in range(n):
        total += mat[i][i] #primary diagonal
        total += mat[i][n-1-i] #secondary diagonal
    if n%2==1:
        total -= mat[n//2][n//2] #remove the middle element if n is odd
    return total

#Example usage
mat1 = [[1,2,3],[4,5,6],[7,8,9]]
result1 = diagonal_sumO(mat1)
print(result1)

mat2 = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
result2 = diagonal_sumO(mat2)
print(result2)