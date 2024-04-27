# For loop 
# For loops can iterate 
name = "Avi"
for i in name:
    print(i)  # Print Avi

colors = ["Red", "Green", "Blue", "Yellow"] # List
for color in colors: # Output would be Red, Green
    print(color)

    for i in color: # Output is breaking down the words to invidual elements, so R e d
        print(i)

# Range()
for k in range(5):
    print(k)   # Output 0 1 2 3 4 5

    # for k in range (1, 20000):
    #     print(k + 1)

    for k in range(1,12,3):
        print(k)