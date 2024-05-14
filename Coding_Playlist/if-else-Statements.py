"""
appleprice = 10
budget = 200

if(budget - appleprice > 50):
    print("Alexa, add 1 kg Apple to the cart.")
elif(budget - appleprice > 70):
    print("its ok you can buy it")
else:
    print("Alexa, do not add apples ot the cart.")


num = int(input("Enter the value of num:"))

if(num < 0):
    print("Number is negative")
elif(num == 0):
    print("number is 0")
else:
    print("number is postive")
"""

# Nested if statements

num = 18

if(num < 0):
    print("Number is negative")
elif(num > 0):
    if(num <= 10):
        print("Number is between 1-10")
    elif(num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")

    

