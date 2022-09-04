class Stack:
    def __init__(self):
        self.__stackList = []
        ## hides the stackList property by placing'__' as a prefix

    def pop(self):
        value = self.__stackList[-1]
        del self.__stackList[-1]
        return value

    def push(self,value):
        self.__stackList.append(value)

# a subclass of the superclass (Stack)

class sub_stack(Stack):

    def __init__(self):
        Stack.__init__(self)
        # here we call the superclass' constructor. This must be done before any initializations in the subclass
        self.__sum = 0
    # the push() function here is being over-ridden.
    # it is the function with the same name as in the superclass
    # BUT, it's functionality has been slightly changed.
    def push(self,value):
        self.__sum += value
        # we invoke the superclass to use the push() function.
        # this is the only way to use the '__stackList' list.
        Stack.push(self,value)
        print("self.__sum:",self.__sum)

    def pop(self):
        sub = Stack.pop(self)
        self.__sum -= sub
        print("Popping:",self.__sum)
        return(sub)
    
    def get_sum(self):
        return self.__sum

stacking = sub_stack()

stacking.push(1)
stacking.push(2)
stacking.push(3)

print("pop:",stacking.pop())

stacking.push(4)
stacking.push(5)
stacking.push(6)

print("pop:",stacking.pop())

# the __sum variable is protected.
# also if we want to get the value of the __sum outside of the class.
# we can use the get_sum() method.

print("From get_sum():",stacking.get_sum())
