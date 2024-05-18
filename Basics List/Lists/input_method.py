#Input Mehtod | Takes unput from the user, user input is alwayus converted to a string 
# By default input method takes input is string
#name = input("Please provide your name: ")

# Converting a input string to integer | Typecasting is needed to convert a string to an integer 
# Input() method can be provided as an argument to the int() method
#number = int(input("Hey enter a number"))


# Problem with an input method 
"""
- Always return input from the user as a string
"""
#numbers = input("Enter a list of numbers: ")
"""
lets say we input 67 48 90 for the input of numbers
# Expected = 67 48 90
index        0   1  2

# Reality = '6''7' '4'8' '9''0'
index        0  1 2 3 4 5 6 7
blank spaces are counted as indicies
"""


# Input a list using loops 

num = int(input("Enter the number of elements: ")) # Typecasting and asking user to enter the nuymber of elements 

number_list = [] # Using the input from num and store it here 

for i in range(num): # basically means that the loop will run according to the user input, for example if user enter 3 the loop will run for 3 times
    x = int(input("Please enter your element: ")) # we want to recieve 3 different inputs, will recieve input from the user
    number_list.append(x)

print(number_list)
