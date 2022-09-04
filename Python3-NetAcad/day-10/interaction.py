def myFunction(myList1):
    print(myList1)
    myList2 = [0, 1]

myList2 = [2, 3]
myFunction(myList2)
print(myList2)


def diffFn(mylist1):
    print(mylist1)
    del mylist1[0]
mylist=[1,2,3]
diffFn(mylist)
print(mylist)

def myFunction(myList1):
    print(myList1)
    #myList1=[6,5,3,4,5]
    del myList1[0]

myList2 = [2, 3]
myFunction(myList2)
print(myList2)
