# More about exceptions

def trythis(number):
    try:
        div = 1 / number
    except ZeroDivisionError:
        print ('Error: Divided by zero.')
        div = None
    # the else statement is always places at the end.
    # it runs if there are no exceptions.
    else:
        print('No Error')
    finally:
        print('finally: i will always run')
        return div

print(trythis(1))
print(trythis(0))
