
def FindMaxB(size, ls):
    max = 0
    for i in range(0,size):
        for j in range(i,size):
            if (max < (abs(ls[i]-ls[j]) + abs(i-j))):
                max = abs(ls[i]-ls[j]) + abs(i-j)
    return max
import sys
def FindMaxO(size, arr):
    '''
    |arr[i]-arr[j] + |i - j| by default we have the given equation to achive the optimize solution we need to remove the abs from the
                                sides then + at one end and - at one end

    Sample Equations
    arr[i]-arr[j] + i - j --> lets bring the i to one side an dj to one side(arr[i]+i -(arr[j]+j))
    arr[i]-arr[j]-i+j --> (arr[i]-i -(arr[j]-j))
    - arr[i]+arr[j]+i-j --> (arr[j]-j -(arr[i]-i))
    -arr[i]+arr[j]-i+j --> arr[j]+j -(arr[i]+i)

    To the above compress equation we take the general equation like this to achive the O(n) complexity
    arr[i]+i
    arr[i]-i
    '''
    max1 = -sys.maxsize
    max2 = -sys.maxsize
    min1 = sys.maxsize
    min2 = sys.maxsize
    for i in range(0, size):
        temp1 = arr[i]+i
        temp2 = arr[i]-i
        max1 = max(temp1, max1)
        max2 = max(temp2, max2)
        min1 = min(temp1, min1)
        min2 = min(temp2, min2)
    return max(max1-min1, max2-min2)
size = int(input("enter the size of array:"))
ls = []
for i in range(0,size):
    ls.append(int(input("Enter the element")))

print(FindMaxO(size, ls))