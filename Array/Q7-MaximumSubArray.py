
"""
Create a function that takes a list of integers as input and returns the maximum sum of any contiguous subarray (a subarray is a contiguous portion of the array). The function should have a time complexity of O(n).
Input 1: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output 1: 6
Explanation 1: The subarray [4,-1,2,1] has the largest sum 6.
"""
def max_sub_arrayB(nums):
    """
    1. Build a prefix array as (pref)
    2. we make pref if length (n+1) with pref[0]=0
    sample pref will be
    index i = 0 1 2 3 4 5 6 7 8
    nums[i] = -2 1 -3 4 -1 2 1 -5 4
    pref index = 0 1 2 3 4 5 6 7 8 9
    pref[i] = 0 -2 -1 -4 0 -1 1 2 -3 1

    3. create varial called max_sum with negative infinity
    4. now we iterate otter loop from range(n), similar to inner loop from range(j+1, n)
    5. in inner loop we calculate current_sum as pref[j+1]-pref[i]
    6. update max_sum as max(max_sum, current_sum)
    """
    n = len(nums)
    #build prefix array
    pref = [0] * (n + 1)
    #create prefix sum array starting from index 1
    for i in range(1, n):
        pref[i+1] = pref[i] + nums[i]
    
    max_sum = float('-inf')
    #iterate over all subarrays
    for i in range(n):
        for j in range(1, n):
            current_sum  = pref[j+1] - pref[i]
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum

def max_sub_arrayO(nums):
    """
    We can use kadane's algorithm to solve this problem in O(n) time complexity.
    1. intialize two variables max_sum and current_sum to nums[0]
    2. iterate through the array from nums[1:]
    3. for each element num, update current_sum as max(num, current_sum + num)
    4. update max_sum as max(max_sum, current_sum)
    """
    if not nums:
        return 0
    max_sum = current_sum = nums[0]
    for i in nums[1:]:
        current_sum = max(i, current_sum+i)
        max_sum = max(max_sum, current_sum)
    return max_sum

#Driven code
if __name__ == "__main__":
    # Example usage:
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print("Maximum Subarray Sum (Prefix Method):", max_sub_arrayB(nums))
    print("Maximum Subarray Sum (Kadane's Algorithm):", max_sub_arrayO(nums))