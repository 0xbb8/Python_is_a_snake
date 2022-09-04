# the lambda function: anonymous function
# lambda parameters : expression

# parameterless anonymous function
two = lambda : 2
# one parameter anonymous function
sqr = lambda x : x * x
# takes two parameters : returns the value of the expression
pwr = lambda x, y : x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))

#NOTE: lambda functions : an anonymous part of code intended to evaluate a result.

