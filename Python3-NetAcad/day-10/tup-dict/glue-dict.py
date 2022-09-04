d1 = {'Adam Smith':'A', 'Judy Paxton':'B+','sas':'bas'}
d2 = {'Mary Louis':'A', 'Patrick White':'C'}
d3 = {}

for item in (d1, d2):
    d3.update(item)
    print(item)
print(d3)
