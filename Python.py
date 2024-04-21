#PYTHON
#SHORTCUTS
"""
* Replicate same lines - alt shift down arrow
* ctrl / for commenting any highlighted code
* hold alt and click on different positions for multuoke cursors
"""

"""
print("Hello World") # To print it on to the terminal
print("Hey I am Avi\nlearning python using escape syquence")   # \n for a new line
print(5+5) # Can also do any calculation simply from print 
print("This is an famous quote \"you have the power to change the world\" by author") #using escape character is backslash to be able to add quotes in code
"""
#GITHUB WORKS
"""
- Source code go to initalize repository 
- U next to file stands for untracked file 
- A next to file strands for file is added in the repository
- Commit it to the repository
- Shift cntrl p for command pallet and type and can create new branch 
- Staging changs is means selecting specific modifications that you want to include in your next commit
- Merge the changes of different branches to the main branch 
- Pull request let you tell other members about the changes you have pushed to a branch in repository on GitHub, alows us to review with collaborators and commits before merging into the base branch
- GitHub Extension allows us to review the changes in depth 
"""

# Variables are containers that hold data 
"""
 a = 1
 b = True 
 c = "Avijot Singh"
 d = None

a = 123456789 # Integer
print(a)
b = "Avi" # String
print(b)
# To determine type of variable 
print("The type of b is:", type(b))
"""
# Operators
"""
Addtion = +
Substraction = -
Multiplication = *
Division = /
Modulus = %
"""

# Excersise 1 - Calculator 
"""
a = 15
b = 20
c = a + b
d = a - b
e = a * b
f = a / b
g = a % b
print("The value of ", a, " + ", b, " = ", c)
print("The value of ", a, " - ", b, " = ", d)
print("The value of ", a, " * ", b, " = ", e)
print("The value of ", a, " / ", b, " = ", f)
print("The value of ", a, " %  ", b, " = ", g)
"""
#Type Casting - Changing datatype
"""
a = "4"
b = "5"
print(int(a) + int(b)) # Using this we are able to convert stirng to integer 

#Two Types of Typecasting 
#1. Explict - As a programmer telling python to convert the datatype to another datatype
#2. Implicit - Python does the conversion

string = "15"
number = 7
string_number = int(string)
sum = number + string_number
print(sum)
"""

#User Input
"""
# Python will take anything as input as a string by default
a = input("Enter your name: ")
print("My name is ", a)

x = input("Enter your first number:")
y = input("Enter your second number:")
print(int(x) + int(y))
"""

#STRING
"""
# ''' quoates makes everything in string
name = "Avi"
friend = "Matt" 
apple = ''' He said, 
Hi Avi
hey i am good 
"I want to eat an apple'''
print(apple)
print("hello", name)
print(name[0]) # First letter of the name variable
print(name[1]) # Second letter of the name variable

# forloop to loop through all the characters
print("lets use forloop\n")
for character in name:
    print(character)

print(len(name)) # To find the length of a variable
print(name[0:2]) # print from 0 to 2 characters in names
"""
#String Methods
"""
# Strings are immutable meaning they cannot be changed once created
a = "Avi"
print(len(a))
print(a.upper())
print(a.lower())
print(a.replace("Avi", "Avijot"))
blogHwading = "introduction to js"
print(blogHwading.capitalize()) # Make the first character in capital also converts other words to lowercase

str1 = "Welcome to the console !!!"
print(str1.endswith("to", 4, 10))
print(str1.find("Welcome"))
"""

#If Else Statements
a = int(input("Enter your age: "))
print("your age is", a)

# Conditional operators, >, <, >=,<=, !=
print(a>18)
print(a>=18)
print(a<=18)
print(a==18)
print(a != 18)
if(a > 18):
    print("you can drive")
else:
    print("you canot drive")


