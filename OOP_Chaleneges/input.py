while(True):
    try:
        name = int(input("What is your age: "))
        print(name)
        break
    except(ValueError):
        print("Please enter a intger | number")