
def kth_bit_set(n, k):
    """
    Check if the k-th bit in the binary representation of n is set (1) or not (0).
    
    :param n: Integer number
    :param k: Bit position to check (0-indexed)
    :return: True if k-th bit is set, False otherwise
    """
    if ((n>>K)&1)==1:
        return True
    else:
        return False
    
def kth_bit_set_alternate(n, k):

    """
    Alternate method to check if the k-th bit in the binary representation of n is set (1) or not (0).
    
    :param n: Integer number
    :param k: Bit position to check (0-indexed)
    :return: True if k-th bit is set, False otherwise
    """
    mask = 1 << k  # Create a mask by left shifting 1 by k positions
    return (n & mask) != 0  # Use bitwise AND to check if the k-th bit is set
       
#Example usage
n = 4  # Binary: 100
K = 2
result = kth_bit_set_alternate(n, K)
print(result)  # Output: True, since the 2nd bit is 1