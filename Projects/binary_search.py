my_list = [3,6,9,13,16,20,24]

x = input("Enter a number: ")

def binary_Search(list,lower_index,higher_index,x):
    if higher_index >= lower_index:
        mid = higher_index + lower_index

