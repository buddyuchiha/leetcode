# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

# Solution 1
def lengthOfLastWord(s: str) -> int:
    counter = 0
    s = s.rstrip()
    s = s[::-1]
    for i in s:  
        if not i.isalpha():    
            return counter
        counter += 1 
    return counter

#
# s = "   fly me   to   the moon  "
s = "a"
print(lengthOfLastWord(s))