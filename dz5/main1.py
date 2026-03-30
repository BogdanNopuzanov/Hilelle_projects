my_string = "I like PHP, PHP, PHP,"

# можна вказувати кілька методів поспіль
my_string1 = my_string.replace("PHP", "Python").replace(',', '!')
print(my_string1) # виведе: I like Python! Python! Python!
