# Important while loop 
# Find orange in the list 
fruits = ['Apple','Mango', 'Bannana', 'Kiwi', 'Aloo','Orange']


index = 0

while(index < len(fruits)):
     if(fruits[index] == 'Orange'):
       
        print("Orange is found")
        break 
     index += 1

else:
    print("orange is not found")