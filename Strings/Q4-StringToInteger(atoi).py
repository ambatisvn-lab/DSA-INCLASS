
"""
Implement the `myAtoi` function which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
The function first discards any leading whitespace characters until the first non-whitespace character is found. Then, it takes an optional initial plus or minus sign followed by as many numerical digits as possible and interprets them as a numerical value.
If the first non-whitespace character is not a valid integer or if no such character exists, the function should return 0. If the integer value exceeds the 32-bit signed integer range, it should be clamped to that range.
The 32-bit signed integer range is [-2^31, 2^31 - 1], which is [-2147483648, 2147483647].
Example 1:
Input: s = "42"
Output: 42  
Example 2:
Input: s = "   -42"
Output: -42
Example 3:
Input: s = "4193 with words"
Output: 4193
Example 4:
Input: s = "words and 987"
Output: 0
Example 5:
Input: s = "-91283472332"
Output: -2147483648
"""
#Brute Force Approach
def myAtoi1(s: str) -> int:
    s = s.lstrip()  # Remove leading whitespace
    if not s:
        return 0

    sign = 1
    index = 0
    if s[0] in ('-', '+'):
        if s[0] == '-':
            sign = -1
        index += 1

    result = 0
    while index < len(s) and s[index].isdigit():
        digit = int(s[index])
        result = result * 10 + digit
        index += 1

    result *= sign

    # Clamp the result to the 32-bit signed integer range
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    if result < INT_MIN:
        return INT_MIN
    if result > INT_MAX:
        return INT_MAX

    return result

#Brute Force approach 2.
def myAtoi2(s: str) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    i = 0
    n = len(s)
    # Discard whitespaces in the beginning
    while i < n and s[i]==' ':
        i += 1
    
    # Check if optional sign if it exists
    sign = 1
    if i < n and s[i] in ('+', '-'):
        if s[i] == '-':
            sign = -1
        i += 1
    
    # collect the digits and ignore non-digit characters
    digit = []
    while i < n and s[i].isdigit():
        digit.append(s[i])
        i += 1
    print(digit)
    
    # return 0 if no digits were found
    if not digit:
        return 0
    
    # Convert collected digits to integer
    num = int(''.join(digit)) * sign

    # Clamp the result to the 32-bit signed integer range
    if num < INT_MIN:
        return INT_MIN
    if num > INT_MAX:
        return INT_MAX
    return num

#optimized approach using Regular Expressions
import re
def myAtoi3(s: str) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    
    # Use regex to find the pattern of optional sign followed by digits
    match = re.match(r'^\s*([+-]?\d+)', s)
    if not match:
        return 0
    
    num_str = match.group(1)
    num = int(num_str)
    
    # Clamp the result to the 32-bit signed integer range
    if num < INT_MIN:
        return INT_MIN
    if num > INT_MAX:
        return INT_MAX
    return num

#optimised Approach.
def myAtoi4(s: str) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    i = 0
    n = len(s)
    # 1. skip spaces
    while i < n and s[i] == ' ':
        i += 1

    # 2. sign
    sign = 1
    if i < n and s[i] in ('+', '-'):
        if s[i] == '-':
            sign = -1
        i += 1

    # 3. parse digits with overflow check
    result = 0
    while i < n and s[i].isdigit():
        digit = ord(s[i]) - ord('0')

        # Check overflow:
        # If result > INT_MAX // 10 OR
        # result == INT_MAX // 10 and digit > INT_MAX % 10
        if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > INT_MAX % 10):
            return INT_MAX if sign == 1 else INT_MIN

        result = result * 10 + digit
        i += 1

    return sign * result

#Example usage
s = "   -42"
print(myAtoi4(s))  # Output: -42
s = "4193 with words"
print(myAtoi4(s))  # Output: 4193
s = "words and 987"
print(myAtoi4(s))  # Output: 0
s = "-91283472332"
print(myAtoi4(s))  # Output: -2147483648