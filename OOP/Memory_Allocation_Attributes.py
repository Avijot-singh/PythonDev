# Different objects have their own memory allocations
# Data -> Attribute
# If there is something common attribute assign it in the class rather than the instance to save memory  
class Students:
    university_name = 'Swinburne University of Technology' # This is a common attribute as all the students are studying at the same university so we don't need to define it into constructor and allocate multiple memory slots to this 
    student_name = "Anonmous"

    def __init__(self,student_name, student_id):
        self.student_name = student_name # obj attribute > class attribute
        self.student_id = student_id
        print(f"Student: {student_name} has been allocated Student ID: {student_id} {Students.university_name}")

s1 = Students('Avijot', 103646287)
# Multiple object = multiple memory slots 
s1 = Students('Virat', 104050664)
print(s1.name) # Will print object attribute as it prioritizes it over class attribute
print('Univeristy: ', Students.university_name) # Can also use s1.university_name both are valid