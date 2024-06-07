#Calculator 

'''
Prompt the user to enter two numbers.
Ask the user to choose an operation (addition, subtraction, multiplication, division).
Perform the selected operation and display the result.

'''
def calculate():
    first_number = float(input("Please enter your first number: "))
    second_number = float(input("Please enter your second number: "))

    print("Available operations: +, -, *, /")
    op = input("Please select an operation: ")

    if op == "+":
        result = first_number + second_number
    elif op == "-":
        result = first_number - second_number
    elif op == "*":
        result = first_number * second_number
    elif op == "/":
        if second_number != 0:
            result = first_number / second_number
        else:
            print("You cannot divide by zero.")
            return
    else:
        print("Invalid operation selected.")
        return

    print(f"The result is: {result}")

while(True):
    calculate()
    user = input("Do you want continue the operation? yes | no : ").lower()
    if(user != "yes"):
        print("bye bye ")
        break
            


