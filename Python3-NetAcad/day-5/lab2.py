hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# put your code here

after_addition = mins + dura
diff = after_addition%60
div = after_addition//60

print (diff, div)
