def pur(prod, price):

    if prod == "shoe":
        tot_price = price - price * 10 / 100

    if prod == "mobile":
        tot_price = price - price * 5 / 100

    print(tot_price)

def ret_prod(prod, price):

    if prod == "mobile":
        tot_price = price - price * 20 / 100

    print(tot_price)

pur("mobile", 3000)
pur("shoe", 300)
pur("mobile", 8000)
ret_prod("mobile", 8000)
