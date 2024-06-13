class Cars:

    discounted_price = 0.8

    def __init__(self,name : str,price : float, quantity : int):
        self.name = name
        self.price = price
        self.quantity = quantity

        assert price >= 0, 'Please enter above 0'
        assert quantity >= 0, 'Please enter above 0'

    def add_cost(self):
        return self.price * self.quantity

    def discount(self):
        self.price *= self.discounted_price


car = Cars('Mercedes', 100, 1)
print(car.add_cost())
car.discount()
print(f'The price after discount', car.price)

