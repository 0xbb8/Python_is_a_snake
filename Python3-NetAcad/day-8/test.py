list=[]
for i in range(10):
    i+=1
    list.insert(i,i*i+i)
print("len():",len(list))
print(list)


myList = [10, 1, 8, 3, 5]
total = sum(myList)

"""for i in range(len(myList)):
    total += myList[i]
"""
print(total)

print("Second face of for loop: check out the code")
calc=0
for i in myList:
    calc+=i
print(calc)

print("Value Swap")
var1=123
var2=456
print("var1:",var1,"var2:",var2)
var1,var2 = var2,var1
print("var1:",var1,"var2:",var2)
