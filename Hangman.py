import random

# library that we use in order to choose
# on random words from a list of words

Name = input("What is your name? \n" )


print("Good Luck ! ", Name)

words = ["random", "enumerate", "dictionary", "qwerty",
         "type", "plasma", "constitution"]


word = random.choice(words)

print("-------------------------------------------------")
print("Guess the characters")

guesses = ''

turns = 10

while turns > 0:


    failed = 0


    for char in word:


        if char in guesses:
            print(char)

        else:
            print("_")


            failed += 1

    if failed == 0:

        print("You Win")

        print("-------------------------------------------------")

        print("The word is: ", word)

        print("-------------------------------------------------")
        break


    guess = input("Guess a character:")


    guesses += guess


    if guess not in word:

        turns -= 1


        print("Incorrect")

        print("-------------------------------------------------")

        print("You have", + turns, 'more guesses')

        print("-------------------------------------------------")

        if turns == 0:
            print("You Loose")
