# Number Guessing 
import random

lower_bound = int(input("Enter your lower bound: "))
higher_bound = int(input("Enter your higher bound: "))

random_number = random.randint(lower_bound,higher_bound)
guesses = 0

while(True):
    user = int(input("Enter your guesss: "))
    if(user == random_number):
        print("YOU GOT IT CONGRATS ")
        break
    elif(user > random_number):
        print("You guessed too high!")
        guesses += 1
        continue
    elif(user < random_number):
        print("You guessed too low!")
        guesses += 1
        continue
print("Guesses took: ", guesses)
        
