# Word Guessing 
import random
words = ["avi", 'singh', 'mandeep','kaur']


name = input("what is your name: ")
print(f'good luck {name}')

random_word = random.choice(words)

print("Start playing")
guesses = ''
turns = 6
while(turns > 0 ):
    failed = 0

    for char in words:
        if char in guesses:
            print(char,end=" ")
        else:
            print("_")
            failed += 1
if failed == 0:
    print("You Win")
    print("The word is: ", words)

