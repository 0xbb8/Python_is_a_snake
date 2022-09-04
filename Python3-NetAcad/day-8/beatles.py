beatles=[]
# step 1
print("Step 1:", beatles)
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
# step 2
print("Step 2:", beatles)
for i in range(2):
    beatles.append(str(input("Enter members: ")))
    # Stu Sutcliffe
    #Pete Best
# step 3
print("Step 3:", beatles)
del beatles[4]
del beatles[3]
# step 4
print("Step 4:", beatles)
beatles.insert(0,"Ringo Starr")
# step 5
print("Step 5:", beatles)

