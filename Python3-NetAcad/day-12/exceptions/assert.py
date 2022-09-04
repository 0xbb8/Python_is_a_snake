from math import sqrt

x = float(input("Enter a number: "))
# throws AssertionError if condition not is not met.
assert x >= 0.0

print("Square root is:", sqrt(x))

# throws an exception if the input data is invalid.
# shows exactly where the problem is.
# Note: does not validate the data or supersede exceptions.
