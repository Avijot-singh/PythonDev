# To change an item, refer to the index of the item 
lists = ["Rob","Avi",1,2, "Bob"]
lists[1] = "Matt"

print(lists)

# Changing Multiple Items 
# In place of a single value, pass a range of values 
l = ["Rob","Avi",1,2, "Bob"]
l[1:3] = ['A','B'] # Here repalceing "Avi" and number 1, 1 index is for "Avi" and 3 is for 1 as last index is always n-1

print(l)

# Inserting a new Item 
# THe insert() method can be used 
# Syntax: list.insert(index,item)

num = ["Rob","Avi",1,2, "Bob"]
num.insert(3,"Singh")
print(num)


#-----------------------------------------------------------------------------------------------------------------------------------------
#Remove Items 
#Remove method 
li = ["Rob","Avi",1,2, "Bob"]
li.remove("Rob")
print(li)

lis = ["Rob","Avi",1,2, "Bob"] # Using the pop method, is used to remove method at the specified index 
lis.pop(1), # if the index of the item is not specified then the last item will be deleted 


# Remove an item using the del keyword, by specifying th eindex 
listss = ["Rob","Avi",1,2, "Bob"]
del listss # Deletes the whole list 
del li[0]

# Clear method to empty the list 
liss = ["Rob","Avi",1,2, "Bob"]

liss.clear()


# Example list
numbers = [10, 20, 30, 40, 50]

# Using pop with an index
removed_element = numbers.pop(2)  # Removes the element at index 2
print("Removed element:", removed_element)  # Output: Removed element: 30
print("List after pop:", numbers)           # Output: List after pop: [10, 20, 40, 50]

# Using pop without an index (removes the last element)
last_element = numbers.pop()
print("Removed last element:", last_element)  # Output: Removed last element: 50
print("List after pop:", numbers)             # Output: List after pop: [10, 20, 40]

# Using remove
numbers.remove(20)  # Removes the first occurrence of 20
print("List after remove:", numbers)  # Output: List after remove: [10, 40]
