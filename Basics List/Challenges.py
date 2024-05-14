# Validate user input excercise

"""
1. username is no more than 12 characters 
2. username must not contain spaces 
3. username must not contain digits

"""

username = input("Enter a username: ")
username.find(" ")
if len(username) > 12:
    print("Your username can't be more than 12 characters")
elif " " in username :
    print("The username cannot have any spaces")
elif not username.isalpha():
    print("your username cannot contain numbers")
else:
    print(f"welcome {username}")
