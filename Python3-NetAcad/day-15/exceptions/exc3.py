# My own exceptions

# NOTE: Custom exceptions are subclasses derived from pre-defined exceptions.

# This sub-class is my custom exception derived from ZeroDivisionError
class OOPS(ZeroDivisionError):
    pass

def doit(boolean):
    if boolean:
        raise OOPS
    else:
        raise ZeroDivisionError

for switch in [False,True]:
    try:
        doit(switch)
    except ZeroDivisionError:
        print('Division by Zero')

for switch in [False,True]:
    try:
        doit(switch)
    except OOPS as e:
        print('My Error')
    except ZeroDivisionError:
        print('Ready-made')
