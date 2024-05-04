#Functions

a = 9
b = 8

gmean = a * b/(a+b)

print(gmean) 

#Creation of Function 

def calculatreGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

if(a > b):
    print("First number is greater")
else:
    print("Second number is greater or equal")


# Function having If else statements within it
def isGreater(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater")


c = 40
d = 50

isGreater(c, d)  


#Two Types of functions :
# Built in functions such as min(), max(), type(), range(), dict()
# User defined functions involve the use of key word def 

#Syntax 
'''
def function_name(parameters):
pass - use pass if it is incompete function and you would want to complete it later
# code and statements
'''


