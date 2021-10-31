from item import Item

class Phone(Item):
    def __init__(self,name:str , price:float, quantity=0,broken_phones = 0):
        #calling super functions have acess to all atributes / methods
        super().__init__(
            name,price,quantity
        )
           
        #run validations to the received arguments
        assert broken_phones >=0,f"broken phones  {broken_phones} is not greater than zero"

        #Assign to self object
        self.broken_phones = broken_phones
