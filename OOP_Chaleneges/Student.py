# Student Challenge 
'''
Create student class that takes name & marks of 3 subjects as arguments in constructor.
Then create a method to print the average.
'''
class Student: 
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def average(self):
        sum = 0
        for val in self.marks:
            sum += val 
        print("hi",self.name,"your avg score is: ", sum/3)
        
    
s1 = Student("Math",[99,76,44]) # We can add a list for three different marks for the marks variable passed in the constructor
s1.average()