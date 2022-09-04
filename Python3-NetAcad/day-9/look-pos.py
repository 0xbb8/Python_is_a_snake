lst = [1,2,3,4,5,6,7,8,9,10]
toFind = 5
pos=0
for i in lst:
    if i == toFind:
        print("Found")
        break
    pos+=1
print("index is:",pos)

# from PCAP the program is:
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
toFind = 5
found = False

for i in range(len(myList)):
    found = myList[i] == toFind
    if found:
        break
if found:
    print("Element found at index", i)
else:
    print("absent")
