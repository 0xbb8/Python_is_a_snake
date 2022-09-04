odd = [1,2,3,4,5]
even = [1,2,3,4,5,6]
len_odd = len(odd)
len_even = len(even)

for i in range(len_odd//2):
    odd[i],odd[len_odd-i-1]=odd[len_odd-i-1],odd[i]
print(odd)

for i in range(len_even//2):
    even[i],even[len_even-i-1]=even[len_even-i-1],even[i]
print(even)
