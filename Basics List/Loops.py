# For Loop
"""
A for loop is used to iuterate over a sequence( such as a list, tuple, or a string )
- Use for loop when you know exactly how many times you want to exexute the loop 
Example:
colours = ["blue","red","orange",purple]
for i in colours:
    print(i)

    hello world
"""





#While Loop
"""
- A while loop is used to repeatedly execute a block of code as long as a certain condition is true
- Use while loop when you don't know how many times you need to execute the loop beforehand
Example:
i = 1
while i< 5:
    print(i)
    i += 1
"""

x = 0 
while (x < 0 or x > 100):
    x = int(input("Please enter number between 0 to 100:"))
print("valid number", x)


"""
- Not condition: This will be True when condition is False. Therefore, the loop runs when the original condition is False
- Loop continues: As long as condition is False, the not condition will be True, and the loop will keep running.
"""
a = -1
while not (0 <= a <= 100):
     a = int(input("Please enter number between 0 to 100:"))
print("valid number", a)

