# More Exceptions
# NOTE: Exceptions are classes.
# When an excption is raised,  an object of the class is instantiated, and goes through all 
# levels of program execution, looking for the except branch that is prepared to deal with it.

try:
    i = int('string')
except Exception as exception:
    # Here 'exception' is used to catch the exception object.
    print(exception)
    print(exception.__str__())
    print(exception.__dir__)
