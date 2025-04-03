# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
# The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

# Solution 1 (long code)
def plusOne(digits: list[int]) -> list[int]:
    number = ''
    for digit in digits: 
        number += str(digit)
    int_number = int(number) + 1
    number = str(int_number)
    digits.clear()
    for num in number: 
        digits.append(int(num))
    return digits

digits = [1, 2, 9]
print(plusOne(digits))

# Solution 2 (attemp to make code shorter)
def plusOne2(digits: list[int]) -> list[int]:
    number = int("".join(map(str, digits)))
    number += 1 
    digits = list(map(int, str(number)))
    return digits

print(plusOne2(digits))
# string.join(iterable) объединяет список в строку.
# s.join(iterable) возвращает строку, которая является результатом конкатенации объекта iterable с разделителем s.
# Обратите внимание, что .join() вызывается строка-разделитель s . iterable должна быть последовательностью строковых объектов.

# Solution 3 making very short and ease
def plusOne3(digits):
    return list(map(int, str(int("".join(map(str,digits))) + 1)))

print(plusOne3(digits))