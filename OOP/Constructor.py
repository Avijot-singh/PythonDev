# Constructor
# Constructor always runs when you call that class using object 
# Constructor always take an argument, which is called self parameter 
# Self basically pointing at the object(instance) you are creating such as s1, so its pointing at that
# if we dont create a constructor python automatically creates it for us 
class Student:
    def __init__(self, fullname, age): # Creating and initializing constructor
        self.name = fullname # This is basically stating that every object will have a different name 
        self.age = age
        print(f"Adding new student: {self.name} aged {self.age} in Databse..")
    

s1 = Student('Avi',10)
print(s1.name)

s2 = Student('Virat',20)
print(s1.age)


# Can also have multiple constructor best practice to have only SINGLE constructor
class Cars:
    # This construtor is called a default constructor
    def __init__(self):
        print("Adding the cars to database")

    # Parameterized constructors
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
c1 = Cars('Mercedes',2020)
print('Your car details', c1.brand, c1.model)
