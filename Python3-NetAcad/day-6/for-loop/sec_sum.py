for i in range(1,11):
    if i%2:print(i)
# another one
uname = ""
for ch in "sandesh@gmail.com":
    if ch == "@":break
    else:uname+=ch
print(uname)
#another one
mod = ""
for digit in "23456789086418300203204":
    if digit == "0":digit="x"
    mod+=digit
print(mod)
# another one
for nums in "2345678098765432256700380304005":
    if nums == "0":
        print("#",end="")
        continue
    else:print(nums,end="")
print()
#another one
n = range(4)
for num in n:print(num-1)
else:print(num)
