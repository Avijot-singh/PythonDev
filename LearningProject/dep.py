import random 

def roll():
    min = 0
    max = 6

    dice = random.randint(min,max)

    print(dice)

roll()
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if(2 <= players <= 4):

            break
        else:
            print("Please enter a number between 2 and 4") 
    else:
        print("Please enter a valid number")
        continue 


max_score = 50
players_scores = [for _ in range(len(players)) ]