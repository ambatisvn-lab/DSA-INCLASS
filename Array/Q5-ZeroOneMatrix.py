
'''
Given a mXn binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.
Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,
0]]
Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
'''
#this will be o(n*m) solution using bfs
from collections import deque
def UpdateMatrix(mat):
    if not mat:
        return mat
    #initialize distance matrix and queue
    rows, cols = len(mat), len(mat[0])
    dist = [[float('inf') for _ in range(cols)]for _ in range(rows)]
    queue = deque()

    #enqueue all 0 cells and set their distance to 0
    for i in range(rows):
        for j in range(cols):
            if mat[i][j]==0:
                dist[i][j]=0
                queue.append((i,j))
    
    #directions for moving up, down, left, right
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    #BFS to update distances
    while queue:
        x,y = queue.popleft()
        for dx,dy in directions:
            new_x, new_y = x+dx, y+dy
            if 0<=new_x<rows and 0<=new_y< cols:
                if dist[new_x][new_y]>dist[x][y]+1:
                    dist[new_x][new_y]=dist[x][y]+1
                    queue.append((new_x,new_y))


    return dist

#Example usage
mat = [[0,0,0],[0,1,0],[1,1,1]]
result = UpdateMatrix(mat)
print(result)