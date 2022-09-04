try:
    print(1/0)
#except ZeroDivisionError:
    #print("Zero")
#except ArithmeticError:
#    print("Arithmetic")
#except Exception:
 #   print("Exception")
except BaseException:
    print("BaseException")
# any one of these exceptions handling is valid as 'ZeroDivisionError' falls
# in the generalized and abstract exception 'ArithmeticError'
# And so on.
# if exceptions all the way up the hierarchy, the first except: statement will run
print("END")
