class item:
    pay_rate = 8
    all = []
    def __init__(self,name:str , price:float, quantity=0):
    #run validations to the received arguments
        assert price >=0,f"price {price} is not greater than zero"
        assert quantity >=0,f"quantity {quantity} is not greater than zero"

        #Assign to self object

        self.name = name
        self.price = price
        self.quantity = quantity


        item.all.append(self)



    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate



item1 = item("Phone",100,1)
item2 = item("Laptop",1000,2)
item3 = item("TV",200,3)
item4 = item("Table",50,4)
item5 = item("Chair",10,5)
