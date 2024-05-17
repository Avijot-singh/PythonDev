#Function
# THey help devide a large program into a smalle rchunks so iuts easier to understand and change 
# Always define functions before calling it

def greet():
    print("hello")
    print("how are you?")

greet()  #Can also call the same fuction multiple times


def hello(name):
    print("hey mate: ", name)

hello("Avi") # Inside the brackets is called an argument so "Avi" is a argument
# When we pass an argument called "Avi" it is passed back to the name variable in function hello and then from there we print that stored variable inside the function 

def addnumber(num1,num2):
    print(num1 + num2)

addnumber(50, 80)

#Another Alternative

def addnumbers(n1,n2):
    result = n1 + n2
    print(f"{n1} + {n2} = {result} ")

number1 = 88.2
number2 = 11.8
addnumbers(number1,number2)

# Or even shorter

def add_number(no1,no2):
    result1 = no1 + no2
    return result1 # Whereever return is called it goes to where it was called in out case it would be line 41

numb1 = 88.2
numb2 = 11.8
result1 = add_number(number1,number2)
print("The sum is", result1)

# Finding lenth of length of a list 

marks = [55,66,77,2,54]

marks_sum = sum(marks)
print("the total number of marks you go is", marks_sum)

"""
THEORY
- A function is a block of code that performes a specific taks. 
- We use the def keyword to define a function
- To bring the function into action we need to call the fucntion. The same function can be called as many times as we want
- We can pass values to a function. THese values passed to functions are called arguments or parameters. 
"""