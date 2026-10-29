# This program analyzes a variable and displays its data type and properties.

a = input(" Enter a value: ")

print( " Value type:" , type(a))
print(" Only spaces? ", a.isspace())
print(" is a number? ", a.isnumeric())
print(" is uppercase? ", a.isupper())
print(" is lowercase? ", a.islower())
print(" is titlecase? ", a.istitle())




      