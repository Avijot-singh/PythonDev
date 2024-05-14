# While Loops

i = 0
while(i<=3):
    print(i)
    i = i + 1
print("Done with the loop")

count = 5 
while (count > 0):
    print(count)  # Will print in reverse order like 5 4 3 2 1
    count = count - 1

else:
    print("I am inside else statement")

    # do {
    #   loop body;

    # }while(condition)

    # Do while loop runs on irrespective to if the condition is true or false

    while True:
        number = int(input("Enter a postive number: "))
        print(number)
        if not number >=0:
    
          break

        