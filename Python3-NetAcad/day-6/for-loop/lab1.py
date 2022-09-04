wordWithoutVowels = ""
userWord = str(input("Enter a word: "))
# Prompt the user to enter a word
# and assign it to the userWord variable


for letter in userWord:
        # Complete the body of the loop.
        letter = letter.upper()
        if letter == "A":
            continue
        elif letter == "E":
            continue
        elif letter == "I":
            continue
        elif letter == "O":
            continue
        elif letter == "U":
            continue
        else:
            wordWithoutVowels+=letter
print ("Word without vowels is:\n"+wordWithoutVowels)
        # Print the word assigned to wordWithoutVowels.
