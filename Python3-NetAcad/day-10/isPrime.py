### By Bosco ###
def isPrime(num):
    divs=0
    #print("num:",num)
    for i in range(2,num):
        #print("i =",i)
        if not num%i:
            #print("IN:",num%i)
            divs+=1
    #print(num,"divs",divs)
    if divs==0:
        return True
    else:
        return False

for i in range(1, 20):
    if isPrime(i + 1):
        print(i + 1, end=" ")
print()
