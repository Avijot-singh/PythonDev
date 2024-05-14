# Lists
# To store multiple values, sperated by commas and changed oppened and closed by brackets
# Can also store multiple different datatypes in the list such as integer and string together
marks = [5,7,7]
num_wor = [6,8,"Avi"]
print(marks[1])
print(type(marks))

Grade = [5,6,8,True, "hey"]

Grade.append("Its appended") # Adding element to the list
Grade.extend(["This is extended", 99,False, 54]) # Can extend the list 
Grade.pop() # Remove the last element in the list
Grade.pop(2) #Can remove a index number
Grade[0] = "Hello" #Replace the index element
print(Grade)