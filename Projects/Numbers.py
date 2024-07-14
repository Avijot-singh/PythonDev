# Numbers
'''
Description: Write a program that performs basic operations on numbers, like addition, subtraction, multiplication, and division.
'''
while(True):
    user_1 = input("Please enter a first number: ")
    if(user_1.isdigit()):
        user_1 = int(user_1)

    user_2 = input("Please enter the second number: ")
    if(user_2.isdigit()):
        user_2 = int(user_2)
        break
    else:
        print("Please enter a integer")
        continue

op = input("Please enter | +, -, *, /")
if(op == "+"):
    result = user_1 + user_2
    print(f'{user_1} + {user_2} = {result}')
elif(op == "-"):
    result = user_1 - user_2
    print(f'{user_1} - {user_2} = {result}')
elif(op == "*"):
    result = user_1 * user_2
    print(f'{user_1} * {user_2} = {result}')
elif(op == "/"):
    result = user_1 / user_2
    print(f'{user_1} / {user_2} = {result} ')