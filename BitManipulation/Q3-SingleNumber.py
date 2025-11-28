
"""
Docstring for BitManipulation.Q3-SingleNumber
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Example 1:
Input: nums = [2,2,1]
Output: 1 
Example 2:
Input: nums = [2,3,5,4,5,3,4]
Output: 2
"""
def single_number(nums):
    """
    Find the single number in an array where every other number appears twice.
    
    :param nums: List of integers
    :return: The single number
    """
    result = 0
    for num in nums:
        result ^= num  # XOR operation to cancel out duplicate numbers
    return result

# Example usage
nums1 = [2, 2, 1]
result1 = single_number(nums1)
print(result1)  # Output: 1

nums2 = [2, 3, 5, 4, 5, 3, 4]
result2 = single_number(nums2)
print(result2)  # Output: 2