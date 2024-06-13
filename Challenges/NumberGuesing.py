import random

print("Welcome to Number Guessing Game")
print('------------------------------------')
guesses = 0
while(True):
    guesses +=1
    a = input('Please enter a number: ')
    if(a.isdigit()):
        a = int(a)
    else:
        print('Please type a number next time')
        continue

    rand = random.randint(0,a)

    if(a == rand):
        print('Correct !!')
        print(f"System {rand}, You {a}")
        print("number of guesses", + guesses)
        break
    else:
        print(f"System {rand}, You {a}")
        if(a > rand):
            print("You were above the number")
        else:
            print("You were below the number")
        
       