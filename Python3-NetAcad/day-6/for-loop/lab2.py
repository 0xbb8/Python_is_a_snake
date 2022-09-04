# Syntactic sugar of the While and for statements

""" 
    The while and the for loop does have a syntactic sugar.
    The function is not quiet unliveable without but is good
    to have in case we need it.
"""

for i in range(5):
    print(i)
else:
    print("else:", i)

i=0
while i<-1:
    print(i)
    i+=1
else:
    print ("else:",i)

i = 111
for i in range (2,1):
    print(i)
else:
    print("Value:",i)

for a in range (2,1):
    print(a)
else:
    print("Non-Existing Value:",a)
    # gives out error as a does not exist if the loop body does not run.
