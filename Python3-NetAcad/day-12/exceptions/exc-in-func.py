# Handled outside function
def funky():
    return 1/0

try:
    funky()
except:
    print("Situation: Handled")

# Handled inside function.
def func():
    try:
        return 1/0
    except:
        print("in func()")

func()

# Exception can cross function() or even module bounds searcing for an except: statement to handle it.
# If not handled, python will through an error message on the console as always.
