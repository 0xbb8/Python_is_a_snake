
blocks = int(input("Enter the number of blocks: "))

#
# Write your code here.
#   
##
star="*"
counter = blocks
while counter != 0:
    
    for i in range(counter):
        print((i+1)*star)
    
    print(counter)
    counter-=1
#

print("The height of the pyramid:", height)
