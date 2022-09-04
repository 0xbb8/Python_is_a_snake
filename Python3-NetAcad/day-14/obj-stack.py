class Stack:
    def __init__(self):
        self.stackList = []

my_stack = Stack()
another_one = Stack()

print("len of my_stack.stackList",len(my_stack.stackList))
my_stack.stackList.append(1)
my_stack.stackList.append(2)
my_stack.stackList.append(3)
my_stack.stackList.append(4)
my_stack.stackList.append(5)

another_one.stackList.append("cat")
another_one.stackList.append("dog")
another_one.stackList.append("person")

print(len(my_stack.stackList))
print(len(my_stack.stackList))
print(my_stack.stackList)
print(another_one.stackList)
