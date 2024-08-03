import random

name = input("Enter your name: ")
print("Good luck!", name)

words = ['Monkey D Luffy','Naruto Uzumaki','Roronoa Zoro','Itachi Uchiha','Bokuto','Son Goku','Ken Kaneki','Vegeta','Madara uchiha','Sosuke Aizen']
word = random.choice(words)
print("Guess the characters")

guesses = ''

turns = 12
while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_")
            failed += 1

    if failed == 0:
        print("You win")
        print("The word is: ", word)
        break

    print()
    guess = input("Guess a character:")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", +turns,"more guesses")

        if turns == 0:
            print("You loose")