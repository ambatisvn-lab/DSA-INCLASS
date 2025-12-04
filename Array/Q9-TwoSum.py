
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""
def two_sumB(nums, target):
    pairs = []
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                pairs.append((i,j))
    return pairs[0] if pairs else None

def two_sumo(nums, target):
    num_map = {}
    for i in range(len(nums)):
        num_map[nums[i]]=i
    for i in range(len(nums)):
        x = target - nums[i]
        if x in num_map and num_map[x] != i:
            return (i, num_map[x])
    return None

#example usage:
nums = [2,7,11,15]
target = 9
print(two_sumB(nums, target))  # Output: (0, 1)