class Pro:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def __str__(self):
        return self.brand+"  "+str(self.price)

    def __add__(self, other):
        return self.brand+other.brand

p1 = Pro("oppo", 46845)
p2 = Pro("oppko", 845)
print(p1+p2)
