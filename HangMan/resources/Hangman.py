#importing the modules
from Dictionary import Dictionary
import random as ran
import time
#welcoming the user
name = input("What is your name? ")
print("Hello " + name, "! Time to play hangman!")
print(" ")
#wait for 1 second
time.sleep(1)
print ("Start guessing...")
time.sleep(0.5)
#here we set the secret
word = (ran.choice(Dictionary))
#creates an variable with an empty value
print(word)
guesses =('')
A = ''
#determine the number of turns
turns = 10
# Create a while loop #check if the turns are more than zero
prin = []
while turns > 0:
    sss = ''
    # make a counter that starts with zero
    failed = 0
    # for every character in secret_word
    for char in word:
        # see if the character is in the players guess
        if char in guesses:
            # print then out the character
            sss += char + " "
        else:
            # if not found, print a dash
            sss += "_ "
            # and increase the failed counter with one
            failed += 1
            # if failed is equal to zero then say it's right
    if failed == 0:
        print(" That's Right!")
    print(sss)
    sss = ''
    # ask the user go guess a character
    win = True
    for char in word:
        if not char in guesses:
            win = False
    if win == True:
        print("\n\nYou Win!")
        time.sleep(3)
        quit()
    guess = input("guess a character:")
    # set the players guess to guesses
    if guess in word:
       guesses += guess
       # if the guess is not found in the secret word
    if guess not in word:
        # turns counter decreases with 1 (now 9)
        turns -= 1
        # print wrong
        print("Wrong ")
        # how many turns are left
        print("You have", + turns, 'more guesses')
    # if the turns are equal to zero
    if turns == 0: # print "You Lose"
        print("\n\nYou Lose...")
        print("\nWord was", word)