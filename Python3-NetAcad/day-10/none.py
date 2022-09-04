def strangeFunction(n):
    if(n % 2 == 0):
        return True
gag = strangeFunction(4)
gaga = strangeFunction(1)
# returns True
print(gag)
# Returns None as an implicit value
print(gaga)

### sum of list
def sum_of_list(lst):
    sum=0
    for item in lst:
        sum+=item
    return sum
result = sum_of_list([2,3,4])
print(result)
# if you call the function like this: sum_of_list(3)
# this will throw an error as single integer value is not iterable

### Function result can be a list

def strangeListFunction(n): # takes n as arguement
    strangeList = []        # makes empty list
    for i in range(0, n):   # loops from 0 to n-1
        strangeList.insert(0, i)    # inserts items in list       
    return strangeList      # returns the list
print(strangeListFunction(5))   # calling the function, passing agrs
