### Average noon temp for whole month
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# the matrix is magically updated here
#
total = 0.0
for day in temps:
    total += day[11]
    average = total / 31
    print("Average temperature at noon:", average)

### The highest temp of the month 
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# the matrix is magically updated here
#
highest = 100.0
for days in temps:
    for temp in days:
        if temp > highest:highest = temp
print ("Highest temperature of the month is:",highest)
### Count days where temp > 20.0
temps = [[0.0 for h in range(24)] for d in range(31)]
#
# the matrix is magically updated here
#
hotDays = 0
for day in temps:
    if day[11] > 20.0:
        hotDays += 1
print(hotDays, "days were hot.")
