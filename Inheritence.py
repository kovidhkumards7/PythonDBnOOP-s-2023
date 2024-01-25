class Phone:

    a = 10  #static or class level variable

    def __init__(self, brand, price, camera):
        self.brand = brand
        self.price = price
        self.camera = camera

    def buy(self):
        print("buying", self.brand)

class FeaturePhone(Phone):

    pass

class SmartPhone(Phone):

    def __init__(self, brand, price, cam, os, ram):
        super().__init__(brand, price, cam)
        self.os = os
        self.ram = ram

    def buy(self):
        super().buy()
        print("buying aaaaaa", self.brand)

    def insure(self):
        print("Insurance of ", self.brand, " phone.")


p1 = SmartPhone("apple", 46456, "15mp", "lollipop", "4gb")
p1.buy()
p1.insure()
print(SmartPhone.a)
