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


car1 = Cars('Mercedes', 100, 1)
car2 = Cars("Audi", 200, 1)
car2 = Cars("BMW", 300, 1)
car2 = Cars("Toyata", 400, 1)

