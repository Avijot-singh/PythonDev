#Function Challenge

#1
"""
Suppose you just attended a University examination The marks you obtained in various subjects are stored in a list like this:

marks = [55, 64, 75, 80, 65]

You want to find the average marks you obtained in the exam. And, based on the average marks you want to find your grade. The grading rule is like this:

You will get Grade A if the average marks is equal to or above 80
You will get Grade B if the average marks is equal to or above 60 and less than 80
You will get Grade C if the average marks is equal to or above 50 and less than 60
And if the average marks is less than 50, you will get Grade F
"""
marks = [55, 64, 75, 80, 65]
def find_average_marks(marks): # Marks as a parmter allows the function to receicve a list of marks, so we can calucate the average of any list of makes
    marks_sum = sum(marks)
    total_subjects = len(marks)
    average_marks = marks_sum / total_subjects
    return average_marks # Return the average marks to where the function was called

# Call the find_average_marks function with the marks list as an argument
# The function executes and returns the average marks, which is then stored in the average_marks variable
def compute_grade(average_marks): # average_marks is a paramter it allows the function to get average marks, so we can callculater the grade
    if average_marks >= 80:
        grade = 'A'
    elif average_marks >= 60:
        grade = 'B'
    elif average_marks >= 50:
        grade = 'C'
    else:
        grade = 'F'
    
    return grade


average_marks = find_average_marks(marks) # Calling the function, marks as the argument
print("Your average marks is: ", average_marks)
grades = compute_grade(average_marks)
print("Your grade is: ", grades)

# Problem 2
"""
Create a program to add and multiply two numbers, by creating to functions add_numbers() and multiply_numbers(). These functions should 
compute the result and return them to the function call, the results should be printer from outside the function
"""

# Addition function
def addition(num1,num2):
    return num1 + num2
    

# Multiply function
def multiply(num3,num4):
    return num3 * num4
    

additions = addition(50,80)
multiplys = multiply(50,10)
#Or
"""
number 1 = 50
number 2 = 60

sum_result = addition(number1, number2)
"""
print(f"Addition result {additions}")
print(f"Multiply result {multiplys}")