
c0 = int(input("Enter non-negative and non-zero integer: "))
i = 0
while c0 != 1:
    if c0<=0:
        c0 = int(input("Enter non-negative and non-zero integer: "))
        continue
    if c0%2==0:c0=(c0/2)
    elif c0%2:c0=(3*c0+1)
    print (int(c0))
    i+=1
else:
    print("You entered 1 you dumbass.")
print("Steps:",i)
