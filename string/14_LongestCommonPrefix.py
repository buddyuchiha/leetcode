# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".


# Solution 1
def longestCommonPrefix(strs: list[str]) -> str:
    str = ""
    if strs.count("") > 0:
        return str
    for i in range (len(min(strs))):
        main_symbol = min(strs)[i]
        for symbol in strs:
            if not symbol[i] == main_symbol:
                return str
        str += symbol[i]
        main_symbol = max(strs)[i]
    return str


# Solution 2 BEATS 100% (CHO YA SDELAL AHAHAHAHAAHHA)
def longestCommonPrefix2(strs: list[str]) -> str:
    res = ""
    if not strs:
        return res
    for i in range(len(min(strs))):
        if not min(strs)[i] == max(strs)[i]:
            return res 
        res += min(strs)[i]
    return res 

                   


strs = ["b"]
strs2 = ["flower","flow","flight"]
print(longestCommonPrefix2(strs))