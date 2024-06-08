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