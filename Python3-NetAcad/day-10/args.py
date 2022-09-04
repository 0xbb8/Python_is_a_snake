def introduction(firstName, lastName):
        print("Hello, my name is", firstName, lastName)
### Positional Arguement Passing ###
introduction("Lex","Luthor")
introduction("Barry","Allen")
### Keyword Arguement Passing ###
introduction(firstName = "James", lastName = "Bond")
introduction(lastName = "Skywalker", firstName = "Luke")

### Mixing Positional and Keyword Arguements ###
def sum(a,b,c):
    print(a, "+", b, "+", c, "=", a + b + c)
# calling funciton sum()
sum(1,2,3)
# But also
sum(4,c=5,b=6)
# don't pass more than one value to a variable like
# sum(1,a=2,b=4) -> Here, value of 'a' is passed more than once.

# Positional arguements must not follow keyword arguements.
def subtra(a, b):
    print(a - b)

subtra(5, b=2)    # outputs: 3
# subtra(a=5, 2)    # Syntax Error

## Also non-default arguement should not follow default arguement.
#def sum(a, b=2, c):
#    print(a + b + c)
#sum(a=1, c=3)
