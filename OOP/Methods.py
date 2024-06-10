# Methods 


class Student:
    def __init__(self, fullname, age, marks): # Creating and initializing constructor
        self.name = fullname # This is basically stating that every object will have a different name 
        self.age = age
        self.marks = marks
        print(f"Adding new student: {self.name} aged {self.age} in Databse..")
    
    def Welcome(self): # Method
        print("Welcome Student")

    def get_marks(self):
        return self.marks


s1 = Student('Avijot Singh', 21, 100)

print(s1.Welcome())
print(s1.get_marks())