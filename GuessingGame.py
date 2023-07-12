from random import randint
number = randint(1, 1000)
question = ("What do you think the number is? ")
print ("I have chosen a number from 1 to 1000, try to guess the number" )
guess = 0
guesses = 0

while True: 
    guess =(int(input(question)))
    if guess < number:
        print(" That number is too low")
        guesses = guesses +1 
    elif guess > number:
        print("That number is too high")
        guesses = guesses +1
        print("Your total number of guesses was " + str(guesses))
    elif guess == number:
        print("That is correct" + guesses)
        break
 
    
 
