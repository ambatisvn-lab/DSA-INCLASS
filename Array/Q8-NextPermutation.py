
"""
Initial array (index annotated)
index:  0  1  2  3  4  5
nums = [1, 2, 3, 6, 5, 4]
Step 1 — Find pivot i (first index from right where nums[i] < nums[i+1])
Scan from right to left comparing neighbors:
compare index 4 & 5: nums[4]=5, nums[5]=4 → 5 < 4? no
compare index 3 & 4: nums[3]=6, nums[4]=5 → 6 < 5? no
compare index 2 & 3: nums[2]=3, nums[3]=6 → 3 < 6? yes
So the pivot index i = 2 and pivot value nums[i] = 3.
... [1, 2,  3,  6,  5,  4]
              ^ pivot i=2 (3)
Step 2 — Find successor j (first index from right where nums[j] > nums[i])
Scan from right to left again:
compare index 5 & pivot: nums[5]=4 > nums[2]=3? yes
So the successor index j = 5 and successor value nums[j] = 4.
... [1, 2,  3,  6,  5,  4]
                      ^ successor j=5 (4)
Step 3 — Swap pivot and successor
Swap the values at indices i and j: nums[i], nums[j] = nums[j], nums[i]
... [1, 2,  4,  6,  5,  3]
Step 4 — Reverse suffix (elements to right of pivot)
Reverse the subarray from i+1 to end of array:
Suffix before reversal: [6, 5, 3]
Suffix after reversal:  [3, 5, 6]
Final array (next permutation): [1, 2, 4, 3, 5, 6]
"""
def next_permutation(nums):
    n = len(nums)
    # Step 1: Find pivot
    i = n-2
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1
    if i >= 0:
        # Step 2: Find successor
        j = n-1
        while nums[j] <= nums[i]:
            j -= 1
        # Step 3: Swap pivot and successor
        nums[i], nums[j] = nums[j], nums[i]
    # Step 4: Reverse suffix
    left, right = i+1, n-1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

# Driven code
if __name__ == "__main__":
    # Example usage:
    nums1 = [1, 2, 3, 6, 5, 4]
    print("Original array:", nums1)
    next_permutation(nums1)
    print("Next permutation:", nums1)