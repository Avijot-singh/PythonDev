# Random Guesing Game
import random

guesses = 0

while(True):
        
        a = input('Please type a number: ')
        
        if(a.isdigit()):
            a = int(a)
            b = random_rand = random.randint(0, a)
            guesses += 1
        else:
            print("please type a number next time: ")
            continue
        

        if(a == b):
            print("Correct !! ")
            print(f'Computer: {b}, You: {a} ')
            print(f'Total number of tries taken {guesses}')
            break
        else:
            print(f'Try again. Computer: {b}, You: {a} ')