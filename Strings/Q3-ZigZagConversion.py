
"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
"""
#optimize solution 
def zigzag_conversion(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s
    
    r , d = 0,1
    grid = ['']*numRows
    for ch in s:
        grid[r]+=ch
        if r == 0:
            d =1
        elif r == numRows-1:
            d = -1
        r+=d
    return ''.join(grid)

#another solution.
def zigzag_conversion2(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s
    
    grid = [['']*len(s) for _ in range(numRows)]
    r , c , d = 0,0,1
    for ch in s:
        grid[r][c] = ch
        if r == 0:
            d =1
        elif r == numRows-1:
            d = -1
        if d == 1:
            r+=1
        else:
            r-=1
            c+=1
    result = ''
    for row in grid:
        for ch in row:
            if ch != '':
                result+=ch
    return result

#another optimize solution.
def zigzag_conversion3(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s
    
    current_row = 0
    going_down = False
    grid = ['']*numRows
    for ch in s:
        grid[current_row] += ch
        if current_row == 0 or current_row == numRows-1:
            going_down = not going_down
        current_row += 1 if going_down else -1
    return ''.join(grid)

#Brute force solution.
def zigzag_conversion_bruteforce(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s
    n = len(s)
    grid = [['']*n for _ in range(numRows)]
    row = 0
    col = 0
    down = True
    for ch in s:
        grid[row][col] = ch
        if down:
            if row==numRows-1:
                down = False
                row -= 1
                col += 1
            else:
                row += 1
        else:
            if row == 0:
                down = True
                row += 1
            else:
                row -= 1
                col += 1
    result = []
    for r in range(numRows):
        for c in range(n):
            if grid[r][c] != '':
                result.append(grid[r][c])
    return ''.join(result)
    
            

# Example usage:
s = "PAYPALISHIRING"
numRows = 3
print(zigzag_conversion(s, numRows))  # Output: "PAHNAPLSIIGYIR"
print(zigzag_conversion2(s, numRows))  # Output: "PAHNAPLSIIGYIR"
print(zigzag_conversion3(s, numRows))  # Output: "PAHNAPLSIIGYIR"
print(zigzag_conversion_bruteforce(s, numRows))  # Output: "PAHNAPLSIIGYIR"

s = "PAYPALISHIRING"
numRows = 4
print(zigzag_conversion(s, numRows))  # Output: "PINALSIGYAHRPI"
print(zigzag_conversion2(s, numRows))  # Output: "PINALSIGYAHRPI"
print(zigzag_conversion3(s, numRows))  # Output: "PINALSIGYAHRPI"
print(zigzag_conversion_bruteforce(s, numRows))  # Output: "PINALSIGYAHRPI"