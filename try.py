class store:
    def __init__(self, pid : int, pname : str, pcost : int, pquan : int, pqual : str):
        #checking the values of arguments
        assert pid >= 100, f"product id {pid} is not valid"
        assert pname is not str, f"product name {pname} is not valid"
        assert pcost >= 1, f"product cost {pcost} is not valid"
        assert pquan >= 0, f"product quantity {pquan} is not valid"
        assert pqual is not str, f"product quality {pqual} is not valid"

        print("inside the constructor")
        print("--------------------")


        #assigning the values
        self.pid = pid
        self.pname = pname
        self.pcost = pcost
        self.pquan = pquan
        self.pqual = pqual

    def pdetails(self):
        print(f"product id : {self.pid}")
        print(f"product name : {self.pname}")
        print(f"product cost : {self.pcost}")
        print(f"product quantity : {self.pquan}")
        print(f"product quality : {self.pqual}")
        print("--------------------")

p1 = store(101,"hrf",465,5,"med")
p2 = store(102,"ef",85,5,"hig")
p3 = store(103,"ahngfed",575,5,"low")
p1.pdetails()
p2.pdetails()
p3.pdetails()