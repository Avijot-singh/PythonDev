# List Comprehension 
# Provides a shorter syntax while creating a new list from the existing list.

names = ['Jimmy','Harj','Kuljit','James','John'] # A names list 
j_names = []

for name in names: # Checking if the names list have any capital J letters and then appending/adding them to our j_names list
    if 'J' in name:
        j_names.append(name)
    
print(j_names)
