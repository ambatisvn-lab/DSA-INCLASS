
"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
input: s = "anagram", t = "nagaram"
output: true
input: s = "rat", t = "car"
output: false
"""
def valid_anagram(s,t):
    if len(s) != len(t):
        return False
    
    freq_s = {}
    freq_t = {}
    for char in s:
        freq_s[char] = freq_s.get(char, 0)+1
    for char in t:
        freq_t[char] = freq_t.get(char, 0)+1
    return freq_s == freq_t

def valid_anagram2(s,t):
    return sorted(s) == sorted(t)

def valid_anagram3(s,t):
    from collections import Counter
    return Counter(s) == Counter(t)

def valid_anagram4(s,t):
    if len(s) != len(t):
        return False
    freq_s = {}
    for char in s:
        if char not in freq_s.keys():
            freq_s[char] = s.count(char)
    
    for char in t:
        if char not in freq_s.keys():
            return False
        else:
            freq_s[char] = freq_s.get(char)-1
            if freq_s.get(char) == 0:
                freq_s.pop(char)
    if len(freq_s) == 0:
        return True
    

# Example usage:
s = "anagram"
t = "nagaram"
print(valid_anagram4(s, t))  # Output: True
s = "rat"
t = "car"
print(valid_anagram(s, t))  # Output: False