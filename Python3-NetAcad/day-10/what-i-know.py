def addition(a,b):
    return a+b
res=addition(b=2,a=5)
print(res)

### returning multiple values
def sq(n1,n2):
    return n1**2,n2**2
squares = sq(2,3)
print("Tuples:",squares)
print ("Unpacking tuples into variables")
var1,var2=sq(2,3)
print(var1,var2)
