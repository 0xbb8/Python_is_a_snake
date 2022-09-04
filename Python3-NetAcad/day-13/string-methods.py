# capitalized the alphabet at index 0 and converts all into lowercase letters
print("capitalize()")
print("hello".capitalize())

# center() centers the string using whitespaces or chars
# the integer provided is the number of whitespaces or chars to include
print("center()")
print("sandesh".center(10))
print("hello".center(10,'#'))

# endswith() - case sensitve method that checks if givens strings ends with give arguement
print("endswith()")
print("MYWorld".endswith('ld'))

# startswith() - case sensitve method that checks if givens strings starts with give arguement
print("startswith()")
print("MYWorld".startswith('m'))

# find() - results the index of the substring in the given string
# -> if provided non existing substring returns -1
print("find()")
print("hello sup homey".find('up'))
print("hello sup homey".find('up',8))
# the second args is the starting index.
print("hello sup homey".find('up',5,9))
# the third index is the limiting index of the search.

# rfind() - right-find() - starts the search from the right side i.e. the largest index
# -> if provided non existing substring returns -1
print("rfind()")
print("hello sup homey".rfind('up'))
print("hello sup homey".rfind('up',8))
print("hello sup homey".rfind('up',5,9))

# isalnum() - is-alphabet-numeric()
# checks if the strings consists of ONLY alphabets and numbers
print('isalnum()')
print('asdfjl@#$%^iasjdf5467'.isalnum())
print("ashdKJHG456KGFYJDJ".isalnum())

# isalpha()
print('isalpha() - checks if string is only alphabet')
print('asdH'.isalpha())
print('asdf%^&23'.isalpha())

#isdigit() - checks if only digit
print('isdigit()')
print('asdfsafd23r'.isdigit())
print('124323'.isdigit())

#islower()
print('islower()')
print('sadfs213fsa'.islower())
print('GH23FHG'.islower())
#isupper()
print('')
print('sadfs213fsa'.isupper())
print('GHFHG'.isupper())
#isspace() - checks for whitespaces
print('isspace()')
print('      \n'.isspace())
print('  asdfa '.isspace())

#join() - concatination with a seperator
print("'list of elements'.join('+')")
print('list of elements'.join('+'))

# lower() - convert all alphabets to lowercase. leave digits and chars alone.
print('lower()')
print('KJGKHDKJHkjhsakjdhk475869@#'.lower())

# upper()
print('upper()')
print('asdGGsad#$%23'.upper())

# swapcase() - lower-to-uppercase and viceversa. digits and chars remain untouched
print('swapcase()')
print('HellO WorLd 2020 is 0n. $#!t'.swapcase())

# title() - convert the first letter in a string to uppercase letter.
print('title()')
print("this is a title of a book".title())

# lstrip() - strip the leading whitespace as defalut or any specified characters of a string.
print('lstrip()')
print("  asdfadf  --".lstrip())
print('www.cisco.com'.lstrip('w'))

# rstrip() - Right-Strip() - opposite of lstrip - removes the trailing char or whitespace.
print('rstrip()')
print("  asdfadf  ".rstrip())
print('www.cisco.com'.rstrip('com'))

# strip() - removes both the leading and trailing whitespaces.
print('strip()')
print('   asdfasdf  '.strip())

# replace() - replaces the specified chars in the string with provided string.
print('"This is awesome".replace("i","$")')
print("This is awesome".replace('i','$'))

# split() - breaks the given string into a list of substrings.
# Assumes the whitespaces in the string as a delimiter.
print('"ths    is awesome,\n innit?".split()')
print("ths    is awesome,\n innit?".split())
print("The Quick Brown Fox Ran Over a Lazy Dog.".split())
