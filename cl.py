class pro:
    dis = 10
    def __init__(self, price):
        self.price = price

    def cost(self):
        tot = self.price - self.price * pro.dis / 100
        print(tot)

    @classmethod
    def en_dis(cls):
        cls.dis = 50    #class method can access only static variables

    @classmethod
    def dis_dis(cls):
        cls.dis = 0


p1 = pro(651)
p1.cost()
pro.en_dis()
p1.cost()
pro.dis_dis()
p1.cost()
