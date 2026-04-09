import string
input_data = input()
start_char, end_char = input_data.split('-')
letters = string.ascii_letters
start_index = letters.find(start_char)
end_index = letters.find(end_char)
result = letters[start_index : end_index + 1]

print(result)