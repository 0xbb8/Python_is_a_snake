class instants():
    
    def __init__(self, val=1):
        self.__first = val

    def set_second(self,val):
        self.__second = 2

first_obj = instants()
second_obj = instants(2)

second_obj.set_second(3)

third_obj = instants(4)
third_obj.__third = 5

print(first_obj.__dict__)
print(second_obj.__dict__)
print(third_obj.__dict__)
# printing the instance variable from outside the class code.
# the variable name is now mangled by python and is now accessible.
# __variable -(after mangling)-> _ClassName__variable
print("first_obj._instants__first:",first_obj._instants__first)
