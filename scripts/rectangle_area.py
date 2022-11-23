import random
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("sorry guess again, too low")
        elif guess > random_number:
            print("sorry too high, guess again")
        #else:
            #print("Correct, you have guessed the number")
    print(f"Coorect you have guesed the number, the number was {x}: ")
#def guess(x):
    #answer = random.randint(1,x)
    #guess = 0
    #while guess != answer:
        #guess = int(input("Enter a number: "))4
        #if x ==answer:
            #print("Correct you got it right ", answer)
            #break
        #elif x > answer:
            #print("Too high")
        #else:
            #print("Too low")


guess(5)
