import string

input_str = input()

for char in string.punctuation:
    input_str = input_str.replace(char, ' ')

result = '#' + ''.join(i.capitalize() for i in input_str.split())

if len(result) > 140:
    result = result[:140]

print(result)