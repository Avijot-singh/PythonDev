import random
#NUMBER GUESSING
r = random.randrange(1, 10) # 10 wont be generated as its n-1 

print('Welcome to the game')

top_range = input("type a number: ")
if top_range.isdigit():
    top_range = int(top_range)
print(top_range)
ra = random.randint(1,10) # 10 will be included in randint
print(ra)