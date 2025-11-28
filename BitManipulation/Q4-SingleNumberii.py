
"""
Docstring for BitManipulation.Q4-SingleNumberii
Given a non-empty array of integers nums, every element appears three times except for one. Find that single one.
Example 1:
Input: nums = [5, 5, 5, 9]
Output: 9
Example 2:
Input: nums = [0,1,0,1,0,1,99]
Output: 99
Approach:
1.Count how many times each bit (0–31) appears.
2.Modulo the count by 3. The bits that are part of the single number will remain.
3.Reconstruct the single number from these bits.

lets use nums = [5, 5, 5, 9] as example
Binary representation:
5 = 0101
9 = 1001
Step1: count bits column wise
Position:   3  2  1  0    (bit index)

Number:     0  1  0  1   (5)
            0  1  0  1   (5)
            0  1  0  1   (5)
            1  0  0  1   (9)
--------------------------------
Totals:     1  3  0  4
Step2: Apply modulo 3
Totals % 3 → remainder bits

1 % 3 = 1
3 % 3 = 0
0 % 3 = 0
4 % 3 = 1
Remainder:  1  0  0  1
Step3: Reconstruct single number from remainder bits
Remainder bits 1001 = 9
"""
def single_number_ii(nums):
    """
    Find the single number in an array where every other number appears three times.
    
    :param nums: List of integers
    :return: The single number
    """
    result = 0
    for bit in range(32):
        count = 0
        for num in nums:
            if (num >> bit) & 1:
                count += 1
        # only the unique number contributes remainder 1
        if count % 3 != 0:
            result |= (1 << bit)

    return result

# Example usage
nums1 = [5, 5, 5, 9]    
print(single_number_ii(nums1))  # Output: 9 