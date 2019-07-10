class a:
    discount = 0.7
    def __init__(self,price):
        self.discount = 0.2
        self.price = price
    def show_price(self):
        return self.price*self.discount
    discount = 0.5
print(a.discount)
print(a(10).discount)
print(a(10).show_price())