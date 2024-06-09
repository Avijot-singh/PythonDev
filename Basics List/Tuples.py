# Tuples 
#Syntax | tuple_name = (item1, item2, item3,...)
# Differece between tuple and list is that tuple has () list has [] and tuple cannot be modified 

cars = ('Audi', 'BMW', 'Mercedes')
print(cars)

# Tuples can have duplicates
names = ('Avi', 'Singh', 'Avi')
print(names)

# Tuple with one item 
colour = ('Red',) # It is important to add comma at the end 
print(colour)

#Length of a Tuple
colours = ('Blue', 'Red', 'Orange')
len(colours)

#Tupple constructor
brand = tuple(('Apple', 'Samsang'))

# Accessing Typle items through postive indexing 
phones = ('Google phones', 'Samsung phones', 'Apple phones')
print(phones[1]) # 0 = Google phones, 1 = Samsung phones, 2 = Apple phones


# Accessing Typle items through negative indexing 
# Index -l refers to the last item, -2 refers to the second last item, and so on.

cars_company = ('Merc', 'Audi', 'BMW')
print(cars_company[-1]) # BMW will be the result

#Accessing Tuple Items through Slicing
# Syntax: tumple_name[index1:index2]

tech = ('Google','Microsoft','Oracle')
print(tech[0:1]) # So basically first number is where to start and last number where to finish, so it excludes Microsoft doesnt run beyond thatm output = Google

# Adding Items to a Tuple
# Not possible to directly add items to tuple as tuples are immutable.
# Although there is a workaround : convert a tuple into a list

temp = list(tech)
temp.append("Corsair")

tech = tuple(temp)
print(tech)

'''
Updating Items of a Tuple
Not possible to directly update items of a tuple as tuples are immutable.
Workaround: Convert a tuple into a list
'''

'''
Removing Items of a Tuple
Not possible to directly remove items of a tuple as tuples are immutable.
Workaround: Convert a tuple into a list
'''
# Unpacking a Tuple
# Packing means assigning values to a tuple.
# Unpacking means extracting values of a tuple.

fruits = ('Mango', 'Banana', 'Apple')
fruit1, fruit2, fruit3 = fruits  # Assinging names to the tuples, fruit1 = Mango, fruit2 = Banana, fruit3 = Apple
print(fruit2)

#Use of Asterisk 
# Used when the number of variables are less than the values of a tuple.

carss = ('Audi', 'Mercedes',' BMW' ,'Toyota', 'Ford')
car1, car2, *car3 = carss # car3 name(variable) will receive  BMW ,Toyota, Ford