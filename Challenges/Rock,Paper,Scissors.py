import random 

user_wins = 0
system_wins = 0
options = ["rock","paper","Scissors"]

while True:
    user_input = input('Type Rock/Paper/Scissors or Q to quit: ').lower()
    if(user_input == 'q'):
        break

    if(user_input not in options):
        continue

    random_number = random.randint(0,2)
    # rock : 1, paper : 1, scissors: 2 
    computer_pick = options[random_number]
    print('Computer Picked', computer_pick + ".")

    if user_input == 'rock' and computer_pick == "scissors":
        user_wins +=1
        print('You win!, Rock over Scissors')

    elif user_input == 'paper' and computer_pick == "rock":
        user_wins +=1
        print('You win!, paper over rock')

    elif user_input == 'scissors' and computer_pick == "paper":
        user_wins +=1
        print('You win!, Scissors over paper')
    
    elif user_input == 'scissors' and computer_pick == "scissors":
        
        print('Draw')
    
    elif user_input == 'paper' and computer_pick == "paper":
        
        print('Draw')
    
    elif user_input == 'rock' and computer_pick == "rock":

        print('Draw')
    

    else: # This cause there is no point checking if the system wins using if conditions as the winning possibilties of the user are already listed
        print("you lost")
        system_wins += 1
    

print(f'You won {user_wins} times')
print(f'computer won {system_wins} times')
print("GoodBye")