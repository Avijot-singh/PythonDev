# Compile time
'''
Syntactical Errors
missing (:)
wrong spelling
'''
# Logical
'''
wrong output
'''
# Run time
'''
divide by zero, getting error at run time, usually user error
'''

a = 5
b = 0

try:
    print("Resouce Open") # Assume that we have an resouce file open

    print(a/b)  #Zero cant be devided so we place try statement, which means that this is critical statement but i am not sure if it will work so try to execute it 
except Exception:
    print("hey, You cannot divide a Number by Zero")

finally: # Finally blockn will be executed if we get error as well as if we dont get the error
    print("Resource Closed") # Good practice to close the resource that you open




try:
    k = int(input("Please enter a number: "))
    print(k)
except Exception: # Exception is global so it knows the type of error, can also replace "Exception" with "valueError": as int inputs have that error type
    print("Please only enter number: ")