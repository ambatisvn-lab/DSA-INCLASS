
"""
You have given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49 
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:
Input: height = [1,1]
Output: 1
"""
#Brute Force method
def Max_water(height):
    n = len(height)
    max_area = 0
    for i in range(n):
        for j in range(i+1, n):
            width = j - i
            ht = min(height[i], height[j])
            area = width * ht
            if area > max_area:
                max_area = area
    return max_area

#optimized method 2pointers:
def Max_water_optimized(height):
    n = len(height)
    left = 0
    right = n-1
    max_area = 0
    while left < right:
        width = right - left
        ht = min(height[left], height[right])
        area = width * ht
        if area > max_area:
            max_area = area
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

#Example usage:
height = [1,8,6,2,5,4,8,3,7]
print(Max_water_optimized(height))  # Output: 49  
