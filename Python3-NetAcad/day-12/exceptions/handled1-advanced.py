# exception handeled individually

try:
    a = int(input("Enter a number(not 0): "))
    print("1/"+str(a)+":",1/a)
# this except: block handles ZeroDivisionError
except ZeroDivisionError:
    print("Can't read, dumbass ???")
# this except: block handles ValueError
except ValueError:
    print("I said a number bitch !!!")
# this will handle both the exceptions
#except (ValueError, ZeroDivisionError):
#    print("Either ValueError or ZeroDivisionError")
except:
    print("Woah! That came outta nowhere ...")
