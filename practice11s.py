class Order:

    def __init__(self, oid, customerName,dishCount, price):

        self.oid = oid
        self.customerName = customerName
        self.dishCount = dishCount
        self.price = price

    def toCSV(self):       # CSV- comma separated values
        return "{},{},{},{}\n".format(self.oid, self.customerName, self.dishCount, self.price)

o1 = Order(1, "John", 3, 450)
o2 = Order(2, "Jennie", 5, 650)
o3 = Order(3, "Jim", 9, 350)

print(o1.toCSV())
print(o2.toCSV())
print(o3.toCSV())

file = open("This PC/Downloads/Orders.csv", "a")
file.write(cppCode)
file.close()
file.write(o1.toCSV())
file.write(o2.toCSV())
file.write(o3.toCSV())
