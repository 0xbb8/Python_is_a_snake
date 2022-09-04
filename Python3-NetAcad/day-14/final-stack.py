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
# first object
stack_object = Stack()

stack_object.push(1)
stack_object.push(2)
stack_object.push(3)
stack_object.push(4)
stack_object.push(5)

# second object
stackObj = Stack()

stackObj.push(stack_object.pop())
print(stack_object.pop())
print(stackObj.pop())
# the stack_object will not be printed as the method is private and the invocation
# is not inside the class body
print(stack_object)
