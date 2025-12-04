"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
"""

def revesre_words(s: str) -> str:
    #return ' '.join(reversed(s.strip().split()))
    a = []
    for i in s.split(' '):
        if i != '':
            a.append(i)
    return ' '.join(a[::-1])

def reverse_word2(s):
    current_word = ''
    final_word=''
    for i in range(0, len(s)):
        if s[i]==' ' and s[i]!='':
            final_word = current_word + ' ' + final_word
            current_word = ''
        if s[i]!=' ':
            current_word = current_word + s[i]
    if current_word != '':
        final_word = current_word + ' ' + final_word
    return final_word[0,len(final_word)-1]
# Example usage:
input_str = "  Hello   World  " 
print(revesre_words(input_str))
