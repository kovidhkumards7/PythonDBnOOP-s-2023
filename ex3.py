class cus:
    def __init__(self, id, name, wallet, addr):
        self.id = id
        self.name = name
        self.wallet = wallet
        self.addr = addr

    def data(self):
        print(self.id, self.name, self.wallet)

    def deliver(self):
        print("delivery address", self.addr.city)



    # def set_wallet(self, wallet):
    #     self.__wallet = wallet
    # def get_wallet(self):
    #     return self.__wallet

class Address:

    def __init__(self, door, street, city, pin):
        self.door = door
        self.street = street
        self.city = city
        self.pin = pin

    def detail(self):
        print(self.door,self.street, self.city, self.pin)

    def deliver(self):
        print("delivery address", self.city)



a1 = Address(314, "7th", "Blore", 48646454)
a1.detail()
a1.deliver()
a2 = Address(5, "5th", "gfsd", 654684)
a2.detail()

c1 = cus(45, "gnjds", 468, a2)
print("name:", c1.name)
c1.name = "fbuycaiwlbnfi"
print("name:", c1.name)
c1.data()
# print(c1.get_wallet())

c1.deliver()