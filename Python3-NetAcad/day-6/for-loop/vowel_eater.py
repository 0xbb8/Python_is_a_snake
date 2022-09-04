userWord = str(input("Enter a word: "))
# Prompt the user to enter a word
# and assign it to the userWord variable.

vowels= ["A","E","I","O","U"]
for letter in userWord:
    letter = letter.upper()
    # Complete the body of the for loop.
    #for i in range(5):
     #   if letter == vowels[i]:break

    if letter == vowels[0]:continue
    if letter == vowels[1]:continue
    if letter == vowels[2]:continue
    if letter == vowels[3]:continue
    if letter == vowels[4]:continue
    
    print(letter)
