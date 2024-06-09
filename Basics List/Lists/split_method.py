# Split method 
# Split method splits a string into a list of substring 
# Syntax : string.split(seperator, maxslit)

senetece = 'I am Avi'
senetece.split()
print(senetece)

#Input a List using Split Method 
# Accepting a list of numbers is easier with split method 
#Create a list of numbers 67,80,95,5

numbers = input("please enter the numbers: ").split()
print(numbers)


"""

"""

for i in range(0,3): # Recieves 2 arguments m to n-1 so range function will return 0 1 2 as the alast value is n-1, basically run the print statement 3 times
    print("hello World")

# Ask the user to input the number of elements they want to enter
n = int(input("Enter the number of elements: "))

# Ask the user to enter the numbers, separated by spaces
# The split() method will split the input string into a list of substrings
number1 = input("Enter the numbers: ").split()

# Loop over the range from 0 to n (number of elements)
for i in range(0, n):
    # Convert each element in the list from a string to an integer
    number1[i] = int(number1[i])

# At this point, number1 is a list of integers
print("List of numbers as integers:", number1)

"""
Explanation of the loop:
1. i will receive the value 0
2. Then, it will get inside the for loop and replace i from both sides by 0:
    number1[0] = int(number1[0])
3. The element at index 0 of number1 is converted from a string to an integer.
4. i will then receive the value 1
5. It will again get inside the for loop and replace i from both sides by 1:
    number1[1] = int(number1[1])
6. The element at index 1 of number1 is converted from a string to an integer.
7. This process continues until i reaches n-1 (the last index).

"""