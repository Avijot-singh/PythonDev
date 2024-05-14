# Equal: ==
# Not Equal: !=
# Less Than: <
# Greater Than: >
# Less Than or Equal to: <=
# Greater Than or Equal to: >=
# Object Identity (Reference Equality): is
# Object Identity (Reference Inequality): is not




language = 'Python'

if language == 'Python':
    print('Language is python')
elif language == 'Java':
    print("Language is Java")
elif language == 'C#':
    print("language is c#")
else:
    print("No match")

user = 'Admin' 
logged_in = True

if user == 'Admin' and logged_in: # Can also use Or / Not
    print('Admin Page')
else:
    print('False Credentials')


a = [1,2,3]
b = [1,2,3]
print(id(a)) # To print out the id
print(id(b))
"""
To assign it be the same id
b = a
"""
print(a == b)
print(a is b) # False as there memory id is different 


# False Values:
# False
# None 
# Zero of any numeric type
# Any empty sequence. For example, '', (), []
# Any empty mapping. For example, {}

"""
condition = False
if condition: 
    print('Evaluates to True')
else:
    print('Evaluates to False')
"""
"""
condition = 0
if condition: 
    print('Evaluates to True')
else:
    print('Evaluates to False')
    """