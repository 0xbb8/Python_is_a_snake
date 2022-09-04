def isYearLeap(year):
    if year%4==0:
        return True
    else:
        return False

def daysInMonth(year, month):
    days=0
    test = isYearLeap(year)
    notLeapMonths=[1,3,4,5,6,7,8,9,10,11,12]
    
    if test == True:
        if month in notLeapMonths:
            days=31
        else:
            days=29
    elif test == False:
        if month in notLeapMonths:
            days=31
        else:
            days=28
    return days

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
    yr = testYears[i]
    mo = testMonths[i]
    print(yr, mo, "->", end="")
    result = daysInMonth(yr, mo)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")
