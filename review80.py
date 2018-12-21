# Take user input.
word = input("Type a word: ")

# Assign length of input to the variable 'length'.
length = len(word)

# Check length of word and print appropriate response.
if length > 5:
    print("Your word is longer than 5 characters")
elif length < 5:
    print("Your word is shorter than 5 characters")
else:
    print("Your word is 5 characters")
