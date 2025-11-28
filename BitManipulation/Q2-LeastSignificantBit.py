
"""
Docstring for BitManipulation.Q2-LeastSignificantBit
Find the position of the first 1 from right to left in the binarty representation of a number n.
input n = 18 (10010)
output = 2 (position of first 1 from right to left is 2nd position
"""
def least_significant_bit(n):
    """
    Find the position of the least significant bit (first 1 from right to left) in the binary representation of n.
    
    :param n: Integer number
    :return: Position of the least significant bit (1-indexed)
    """
    if n == 0:
        return 0  # No bits are set in 0
    else:
        position = 1
        for i in range(32):  # Assuming a 32-bit integer
            if (n & (1 << i)) == 0:
                position += 1
            else:
                break
        return position
    
# Example usage
n = 18  # Binary: 10010
result = least_significant_bit(n)
print(result)  # Output: 2, since the least significant bit set is at position 2