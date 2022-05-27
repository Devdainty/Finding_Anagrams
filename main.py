# Check if a word is an anagrams
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word1, word2):

    # use sorted() to sort both the strings into lists.
    # Compare the sorted lists and check if they are equal.
    # return True if they are equal

    if(sorted(word1) == sorted(word2)):
        return True
    else:
        return False


# Take two strings from the user and store them in separate variables.
word1 = input('Enter the first word : ')
word2 = input('Enter the second word : ')

# print out words entered by the user
print('First word is : ' + word1)
print('Second word is : ' + word2)

# assign the returned boolean to a variable so it can be printed
output = find_anagrams(word1, word2)

# print the returned value
print(output)

if output == True:
    print(word1 + ' and ' + word2 + ' are anagrams.')
else:
    print(word1 + ' and ' + word2 + ' are not anagrams.')
