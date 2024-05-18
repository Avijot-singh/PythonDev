# List

"""
THEORY
- A  collection of similar or different types of data items
"""
# Creating List - A list is created by placing items inside [] seperated by commas
numbers = [1,2,3,4,5,6,7,8,9,10] # numbers is the variable which is storing and pointing to this list 

# Empty List 
num = [] # Without any items 

# List can include duplicate numbers

n = [1,2,1,2,3,3,4,4,5,5]

# A list with different types of items

items = [1,2,'N','Go',3.14159]

#Features of a list 
"""
1. A list can have duplicate items
2. Items in a list are mutable/changeble
3. Lists can store items of various types
"""

 # -------------------------------------------------------------------------------------------------------------------------------------------------------
 # Single-Dimensional list(Normal list)
 # Accessing elements of a Single-dimensional List



"""
 - A singlw-dimentsional list is a list where elements are listed one after the other
 - Each element is allocated a unique number called index
 """

my_list = [5,10,15,20]
# Index    0  1  2  3

# To access the first number 
print(my_list[0])

# Negative indexing | Accessing elements from the last 

MyList = [5,10,15,20] # Python also has negative indexing
#Index   -4 -3 -2 -1
print(MyList[-1])

# MULTI-DIMENSIONAL LIST 
# Accessign elements of a Multi-Dimensional list
"""
- Multi-dimentsional list is a list ocntaining another list
- Example:
my_list = [[1,2,3,"neso", [4,5,6]]     ---Visual Representation of this---
          ________  ________ ________
          |      | |       | |       |
          |      | |       | |       |
          |      | |       | |       |
          --------  --------  ------- 
Index         0        1         2


my_list have a total of 3 memory blocks as it has 3 elements example first element has 3 items 

-First memory block will have [1,2,3]
- Second memory block will have "Neso"
- Third memory block will have [3,5,6]

To access lets say 1
print(my_list[0][0]) Result will be 1

To access the whole list 
my_list[2]  Result will be [4,5,6]
"""