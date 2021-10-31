import csv
class Item:
    pay_rate = 0.8
    all = []
    def __init__(self,name:str , price:float, quantity=0):
    #run validations to the received arguments
        assert price >=0,f"price {price} is not greater than zero"
        assert quantity >=0,f"quantity {quantity} is not greater than zero"

        #Assign to self object

        self.__name = name
        self.__price = price
        self.quantity = quantity

        #actions to execute
        Item.all.append(self)

    @property
    def price(self):
        return self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self,increment_value):
        self.__price = self.__price + self.__price * increment_value



    @property #property Decorator = Read only Attribute
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        #we can also riase exception if we want
        if len(value) > 10:
            raise Exception("the name is too long")
        else:
            self.__name = value


    #decorators to change to class method
    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            #readcontant as list of dictionary
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            #creating instances
            Item(
                #reading from dictionary keys
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    #writing a static method to check weather a number is recived is integer or not
    @staticmethod
    def is_integer(num):
        #We will count out the floats that arepoint to zero
        #For i.e: 5.0,10.0
        if isinstance(num,float): #to check recived parameter is an instance of float or integer
            #count out the floats that arepoint zero
            #countout the floats that are pointzero
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False



    def __repr__(self):
        return f"item {self.__class__.__name__}('{self.name}','{self.__price}','{self.quantity}')"

