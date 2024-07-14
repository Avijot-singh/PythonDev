class Dog(object):
    def __init__(self, name):
        self.name = name
        print("Made a dog")
    
    def speak(self): # This is a method as it is associated inside a class and has self in params
        print(f'Hey I am {self.name}')

avi = Dog('Avi')
avi.speak()
