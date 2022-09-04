dict = {"cat" : "chat", "dog" : "chien", "horse" : "cheval"}
print(dict)

# adding KV pair
dict['swan'] = 'french-swan'
print(dict)

# edit KV pair
dict['swan'] = 'cygne'
print(dict)

# update using update() method
dict.update({'cat':'biralo'})
print(dict)

# delete KV pairs using 'del' instruction
del dict['cat']
# also using popitem() : deletes last item in dictionary
dict.popitem()
print(dict)
