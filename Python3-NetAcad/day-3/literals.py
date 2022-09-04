# Python Literlas

print ("123")
print (123)

# these are different as they are stored in computer's memory differently.
# the first one is called a string literal and second one is a numeric literal.
# Literals are self defining data.

# Python3.6 allows the use of underscores in numeric literals.

print (123456789) 
 
print (-987654321)

# a negative number is noted in python as by adding a -ve sign as prefix.

# print() function converts octal and hexa-decimal numeric literals into decimal.
# It uses special prefixes to determine the type of integer.
# 0o OR 0O (Zero - o/O) -> Octal
# 0x OR 0X (Zero - x/X) -> Hexa-Decimal

print (0o123)
print ("0o123 octal is converted into decimal")

print (0x123)
print ("0x123 hexa-decimal is converted into decimal")

# Floats : Non-empty decimal fractions
# NOTE: 4.0 and 4 are not the same. As one is stored as a float and the other as an integer.
print ("Floats:", -3.2, 4.3, 0.4, .4,4.0,4., sep=", ")

# Exponent in python.
# 3 x 10^8 can be represented in python as 3E8.The result is a float.The base MAY BE and integer but the exponent MUST BE and integer.
# 'E' is called an exponent i.e. 'times 10 the power of'

print (3E4)
print (3e6)

#Planck's Constant (h) = 6.62607 x 10^-34

print (6.62607E-34)
print (0.000000000000000000000000000000000662607)
# Python choses the most economical representation of a literal.

print ('Python is named after "Monty Python"')
print ("Python is named after \"Monty Python\"")


# Booleans in python. Represented by True and Flase.

print (True > False)
print (True < False)

#There is one more, special literal that is used in Python: the None literal.
#This literal is a so-called NoneType object, and it is used to represent the absence of a value.

print (None)
