### Your task is to write and test a function which takes three arguments 
### (a year, a month, and a day of the month) and returns the corresponding day of the year,
### or returns None if any of the arguments is invalid.

def isYearLeap(year):
    if year%4 == 0:
        #print(year%4)
        return True
    else:
        #print(year%4)
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
    else:
        days=None
    return days
def dayOfYear(year, month, day):
    res=0
    ld=[31,29,31,31,31,31,31,31,31,31,31,31]
    nld=[31,28,31,31,31,31,31,31,31,31,31,31]
    if day<1 or day>31:
        print("1")
        print(day)
        res=None
    elif month<1 or month>12:
        print("2")
        res=None
    elif year<0:
        print("3")
        res=None
    else:
        feb=daysInMonth(year,month)
        for i in range(month-1):
            print("itr",i)
            if feb==28:
                res+=nld[i]
                print("nld",nld[i])
            else:
                res+=ld[i]
                print("ld:",ld[i])
            print("res:",res)
    return res+day
print(dayOfYear(2020, 4, 6))
