class Order:

    def __init__(self, oid, customerName,dishCount, price):

        self.oid = oid
        self.customerName = customerName
        self.dishCount = dishCount
        self.price = price

o1 = Order(1, "John", 3, 450)
o2 = Order(2, "Jennie", 5, 650)
o3 = Order(3, "Jim", 9, 350)

print(o1.__dict__)
print(o2.__dict__)
print(o3.__dict__)

