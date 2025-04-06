# Solution 1
def romanToInt(s: str) -> int:
    symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    main_symbols = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    number = 0
    while len(s) != 0:
        if len(s) == 1:
            number += symbols.get(s[0])
            return number
        string = s[0] + s[1]
        if main_symbols.get(string):
            number += main_symbols.get(string)
            s = s[2:]
        else:
            number += symbols.get(s[0])
            s = s[1:]
    return number

s = "MCMXCIV"
print(romanToInt(s))