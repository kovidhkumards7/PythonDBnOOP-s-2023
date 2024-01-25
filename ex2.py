class product:
    discount = 10  # static or class level variable

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def purc(self):
        print("purchasing", self.brand)
        tot = self.price - self.price * product.discount / 100
        print("Final Price of ", self.brand, "is :", tot)

    def ret(self):
        print("returning", self.brand)

    @staticmethod
    def en_dis():
        product.discount = 20

    @staticmethod
    def dis_dis():
        product.discount = 0


print("normal season")
p1 = product("oppo", 8146, 10)
p1.purc()
p1.ret()

print("festive season")
product.en_dis()
p1.purc()
p1.ret()

print("without discount")
product.dis_dis()
p1.purc()
p1.ret()

print(product.discount)
