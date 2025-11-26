"""
Brute-force solution for LeetCode 42 - Trapping Rain Water

Approach (brute force):
For each position i, find the highest bar to the left (including i) and
the highest bar to the right (including i). The water that can be trapped
on top of i is max(0, min(max_left, max_right) - height[i]).

Time complexity: O(n^2) in worst case because for each index we scan left and right.
Space complexity: O(1) extra space.
"""

from typing import List

def trap_bruteforce(height: List[int]) -> int:
	"""Return how much water can be trapped using brute-force method.

	Args:
		height: list of non-negative integers representing elevation map.

	Returns:
		Total units of trapped water (int).
	"""
	n = len(height)
	if n <= 2:
		return 0

	total = 0
	for i in range(n):
		# find max to the left of i (including i)
		max_left = 0
		for l in range(0, i + 1):
			if height[l] > max_left:
				max_left = height[l]

		# find max to the right of i (including i)
		max_right = 0
		for r in range(i, n):
			if height[r] > max_right:
				max_right = height[r]

		# water at i is bounded by the shorter side
		water_at_i = min(max_left, max_right) - height[i]
		if water_at_i > 0:
			total += water_at_i

	return total

def trap_2pointers(height: List[int]) -> int:
    n = len(height)
    if n <= 2:
        return 0

    left = 0
    right = n - 1
    left_max = 0
    right_max = 0
    total = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                total += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                total += right_max - height[right]
            right -= 1

    return total



if __name__ == "__main__":
	# Example test cases
	tests = [
		([0,1,0,2,1,0,1,3,2,1,2,1], 6),
		([4,2,0,3,2,5], 9),
		([], 0),
		([1,2,3], 0),
	]

	for arr, expected in tests:
		result = trap_2pointers(arr)
		print(f"height={arr} -> trapped={result} (expected={expected})")

