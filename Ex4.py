class Customer:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def pay(self, payment):
        print(payment.type, payment.price)


class Payment:

    def __init__(self, type, price):
        self.type = type
        self.price = price



p1 = Payment("upi", 1521)
c1 = Customer(45, "feagf")
c1.pay(p1)