# Variables in python
# They are containers with variable content.
# Python is a dynamically typed language. So, there is no need to declare variables.
var = 1234
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)

string_var="3.5.3"
print ("Python version" , string_var)

john = 3
mary = 4
adam = 6

print (john, mary, adam, sep=", ")
totalApples = john + mary + adam
print ("Total number of apples: ", totalApples)

x = 45
x+=5
print(x)

# EXAMPLES - Shortcut Operators

# i = i + 2 * j ⇒ i += 2 * j

# var = var / 2 ⇒ var /= 2

# rem = rem % 10 ⇒ rem %= 10

# j = j - (i + var + rem) ⇒ j -= (i + var + rem)

# x = x ** 2 ⇒ x **= 2


kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles*1.61
kilometers_to_miles = kilometers/1.61

print(miles, "miles is", round(miles_to_kilometers, 3), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
