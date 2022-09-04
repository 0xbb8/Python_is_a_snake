def isYearLeap(year):
    if year%4 == 0:
        print(year%4)
        return True
    else:
        print(year%4)
        return False
#
# put your code here
#

testData = [1900, 2000, 2016, 1987, 2021]
testResults = [False, True, True, False, False]
for i in range(len(testData)):
    yr = testData[i]
    print(yr,"->",end=" ")
    result = isYearLeap(yr)
    print(result)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")
