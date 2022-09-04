num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

if num1 > num2:
    if num1 > num3:
        biggie = num1
elif num2 > num3 : biggie = num2
else : biggie = num3

print ("Largest number is:", biggie)
# using buint-in max( function)
print ("max():", max(num1,num2,num3))
# using min()
print ("min():", min(num1,num2,num3))
