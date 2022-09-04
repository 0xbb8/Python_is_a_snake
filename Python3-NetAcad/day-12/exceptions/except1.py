a = int(input("Enter first value: "))
b = int(input("Enter second value: "))

try:
    print("a/b: ",a/b)
    print("This line does not get printed.")
except:
    print("Nope that's wrong")
print("This is after the except: block")
