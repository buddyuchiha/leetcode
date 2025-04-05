def longestCommonPrefix(strs: list[str]) -> str:
    str = ""
    j = 
    if strs.count("") > 0:
        return str
    for i in range (len(min(strs))):
        main_symbol = min(strs)[i]
        for symbol in strs:
            if not symbol[i] == main_symbol:
                return str
        str += symbol[i]
        main_symbol = max(strs)[i+1]
    return str

strs = ["b"]
print(longestCommonPrefix(strs))