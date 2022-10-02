class Wallet:
    def __init__(self, money = 0):
        self.money = money

    def credit(self, amount):
        self.money += amount
        print(f"Your money {self.money} ")
        

    def debit(self, amount):
        self.money -= amount
        print(f"Your money {self.money} ")
    
    def __str__ (self):
        return f"{self.money}"

class Person:
    def __init__(self, name, location, money):
        self.name = name
        self.location = location
        self.wallet = Wallet(money)
    

    def moveTo(self, point):
        self.location = self.point

    def __str__ (self):
        return f"Hi I'm {self.name}, and my location is {self.location} I have {self.wallet.money} in my bank"


class Vendor(Person):
        range = 5
        price = 1
        
        def __init__(self, name, location, money):
            super().__init__(name, location, money)


        def sellTo(self, customer, number_of_icecreams):
           self.moveTo(customer.location)
           self.wallet.credit(self.price * number_of_icecreams)
           customer.wallet.debit(self.price * number_of_icecreams)


class Customer(Person):
    def __init__(self, name, location, money):
        super().__init__(name, location, money)


    def _is_in_range(self , vendor):
        if abs(self.location - vendor.location) <= vendor.range:
            return True
        else:
            return False

    def _have_enough_mony(self, vendor, number_of_icecreams):
        if self.wallet.money >= (vendor.price * number_of_icecreams):
            return True
        else:
            return False

    def _request_icecream(self, vendor, number_of_icecream):
        if self._is_in_range(vendor) and self._have_enough_money(vendor, number_of_icecream):
            vendor.sellTo(self, number_of_icecream)
