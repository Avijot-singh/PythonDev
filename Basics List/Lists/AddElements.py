# Adding Elements to a List
#Elements can be added to a list in different weays, following are the methods to add elements to a list.
# Append() Method, Insert () Method, Extend() Method

# append Method | A built-in method used to add an item at the end of a list 
lists =  [1,2,3,4,5]
lists.append(6) # Adds the number 6 at the end of the list

# Duplicate append() method to add multiple times
lists.append(7)
lists.append(8)


# A List as an item in this list which means adding an list to the current list
lists.append([3,5,6])

print(lists) # Result [1, 2, 3, 4, 5, 6, 7, 8, [3, 5, 6]]


# Insert Method | A built-in method used to add an item at a specific position
my_list = [1,4,5,'Avi']
# syntak list_Name(position, value)
my_list.insert(0,'Python')
print(my_list)

# Extend Method | A built-in method used to add all items of one list in another list 
# Syntac List1.extend(list2)
#Useful in merging lists together
list1 = [1,2,3,4,5]
list2 = ['Avi','Singh','Python']
list1.extend(list2)
print(list1)