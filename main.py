class Item:

    pay_rate = 0.8
    
    def __init__(self, name=str, price=float, quantity=0):

        assert price >= 0, f"Price {price} is not greater than 0"
        assert quantity >= 0, f"Quanity {quantity} is not greater than 0"
        
        self.name = name
        self.price = price
        self.quantity = quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate


item1 = Item("computer", 100, 10)
print(item1.pay_rate)
print(Item.__dict__)
print(item1.__dict__)
item1.apply_discount()
print(item1.price)
