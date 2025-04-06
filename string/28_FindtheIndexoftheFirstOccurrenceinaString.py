# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Solution 1, wtf?
def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)

# Default CMP Algrotihm
def strStr(word, text):
    n = len(text)
    m = len(word)

    if m == 0:
        return 0  # Пустая строка всегда находится в начале

    if n == 0:
        return -1 # В пустой строке нечего искать

    pi = [0] * m
    j = 0
    i = 1
    while i < m:
        if word[j] == word[i]:
            pi[i] = j + 1
            i += 1
            j += 1
        elif j == 0:
            pi[i] = 0
            i += 1
        else:
            j = pi[j - 1]

    # 2. Поиск образца в тексте
    i = 0  # Индекс по тексту
    j = 0  # Индекс по образцу
    while i < n:
        if text[i] == word[j]:  # Сравнение text[i] с word[j]
            i += 1
            j += 1

            if j == m:
                return i - m  # Образец найден! Возвращаем индекс начала вхождения
        else:
            if j > 0:
                j = pi[j - 1]
            else:
                i += 1

    return -1  # Образец не найден

# Solution 2
haystack = "sadbutsad"
needle = "ssad"
print(strStr(haystack, needle))