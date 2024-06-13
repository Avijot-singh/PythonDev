class Item:
    pay_rate = 0.8 # The pay rate after 20% discount | This is class level attribute so it shared among all instances 

    def __init__(self, name : str, quantity, price : float): # The str and float after : are there tp indicate what value you explect to be entered in those variables
        print(f'I am a constructor, I am created everytime a new instance is created: {name}')
        # Run validations to the received arguments
        # assert keyword is used to set a condition that must be true, and if the condition is false, it raises an AssertionError exception
        assert price >= 0, "price cannot be negative"
        assert quantity >= 0

        # Assigned to self objects
        self.quantity = quantity # Reason we create instance variable rather than local variables are beacause there accessible all around the class.
        self.price = price
        self.name = name
        
        

    def calculate_total_price(self): # Self is there to target the instance
        return self.price * self.quantity 
    
    def apply_discount(self):
         self.price = self.price * self.pay_rate
    
# print(Item.__dict__), __dict__ is useful to lkist all the attributes, in this case it will list all the attributes for Class Level

I1 = Item("Phone", 1, 100)
print(f"{I1.name}, Price + Quantity: ",I1.calculate_total_price()) 
I1.apply_discount()
print(f"price after discount: {I1.price}")

I2 = Item("Laptop", 1, 1000)
I2.pay_rate = 0.7 # It is an instance level attribute specific to this I2 
a = I2.calculate_total_price()
print("Total cost is :", a )
I2.apply_discount()
print("After discount it is: ", I2.price) 

# on 51 minute