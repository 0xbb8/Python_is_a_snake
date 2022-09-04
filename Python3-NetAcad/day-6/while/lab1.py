# odd and even counter

odd, even = 0, 0

number = int(input("Number (0 to exit): "))
counter=6
while counter:
    # while number != 0
    if number % 2:odd+=1
    # if number % 2 == 1: odd = odd + 1
    else:even+=1
    number = int(input("Number (0 to exit): "))
    counter-=1
print ("Odd numbers:", odd)
print ("Even numbers:", even)
