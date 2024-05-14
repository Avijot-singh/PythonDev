name = input("Hey what is your name: ")
phone_number = input("What is your number:")
#result = len(name) # Lenth of the input name
result1 = name.find("i") # Finding space or any characters
#result2 = name.rfind("o") # This is in reverse order 
#name = name.capitalize()
#name = name.upper()
#name = name.lower()
#result = name.isdigit() # It is to find if there are any integers only 
#result = name.isalpha() # It is to find if there are any strings only
result = phone_number.count("-")
print(result1)
print(result) 