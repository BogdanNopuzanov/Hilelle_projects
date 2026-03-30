import string
import keyword

str1 = input()

fpunctuation = string.punctuation.replace('_', '')

bool1 = (
    not str1[0].isdigit() and
    not any(char.isupper() for char in str1) and
    all(char not in fpunctuation for char in str1) and
    ' ' not in str1 and
    str1 not in keyword.kwlist and
    str1.count('_') <= 1
)

print(bool1)