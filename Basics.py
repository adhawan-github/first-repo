"""
NOTE: Three double quotes are for multi line comments.
# is for single line comments
"""

# ------------------------------------------
# This is to type Hello World
print("Hello World!")
# ------------------------------------------

# ------------------------------------------
# The below lines are to explain how:
# (1) Variables are defined
# (2) Typecasting can be done
# (3) How to add/subtract etc

x = 1
X = '2'
print(x, X, X, x)

print(x + int(X))
print(type(X))
_variable_name = "Python Variable Name"

print(_variable_name)

_vAriable_name = 1

print(_variable_name)

fl = 1.5

print(x - fl)
# ------------------------------------------

# ------------------------------------------
# The below lines explain how to print single and double quotes

print('These are "double quotes"')
print("These are 'single quotes'")
print('These are "double quotes" and these are \'single quotes\' in the same sentence')
print("These are 'single quotes' and these are \"double quotes\" in the same sentence")

# ------------------------------------------
name = 'Anirudh'

# This cannot print successfully if name is not a string
# This is because the + makes this an addition/concatenation operation
print('Hi ' + name)

# This can print anything successfully even if name is a string
# This is not adding/concatenating so that problem never occurs
print('Hi', name)

# This can also print anything successfully even if name is a string
# This does not add/concatenate either so that problem never occurs
print(f'Hi {name}')

# {} here holds the variable you specify
print('Hi {}!'.format(name))

# Using print with format within {}
print('Hi {:>25}!'.format(name))
print('Hi {:^25}!'.format(name))
print('Hi {:25}!'.format(name))
print('Hi {:^25.3}!'.format(name))

# Using format to print multiple variables using arguments
a = 5
b = 10
print('{},{}'.format(a, b))
print('{0},{1}'.format(a, b))
print('{1},{1}'.format(a, b))
print('{0},{0},{1},{1},{1},{1},{0},{0}'.format(a, b))

# ------------------------------------------

# this is a list - python's version of an array
list_fruits = ['apple', 1.5, 1, 'apple', 'banana', 'strawberry', 2.5, 'grapes', 'watermelon', 2, 3]
print(list_fruits)
print(list_fruits[0])
print(list_fruits[2])
print(list_fruits[6])

# Use -1 for last value of list. -2 for second last and so on
print(list_fruits[-1])

# this is a dictionary - apple points to red, banana points to yellow and so on
dict_fruits = {'apple': 'red', 'banana': 'yellow', 'strawberry': 'more red', 'grapes': 'purple', 'watermelon': 'who cares'}
print(dict_fruits)

# this is to illustrate how the latest value is always kept in a dictionary
# apple and green have overwritten apple and red
dict_fruits = {'apple': 'red', 'apple': 'green', 'banana': 'yellow', 'strawberry': 'more red', 'grapes': 'purple', 'watermelon': 'who cares'}
print(dict_fruits)
print(dict_fruits['apple'])
print(dict_fruits['apple'])
print(dict_fruits['apple'])
print(dict_fruits['apple'])
print(dict_fruits['apple'])
print(dict_fruits['apple'])
