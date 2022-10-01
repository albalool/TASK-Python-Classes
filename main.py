from http.client import NON_AUTHORITATIVE_INFORMATION


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
    def __init__(self, name, location, wallet):
        self.name = name
        self.location = location
        self.wallet = Wallet(wallet)
    

    def moveTo(self, point):
        self.point = point
        self.location = self.point

    def __str__ (self):
        return f"Hi I'm {self.name}, and my location is {self.location} I have {self.wallet} in my bank"


class Vendor(Person):
    def __init__(self, name, location, wallet, range = 5 , price = 1):
        super().__init__(name, location, wallet)
        self.range = range
        self.price = price

    def sellTo(self, customer, number_of_icecreams):
        self.moveTo(customer.location)
        self.wallet.credit(self.price * number_of_icecreams)
        customer.wallet.debit(self.price * number_of_icecreams)


class Customer(Person):
    def __init__(self, name, location, wallet):
        super().__init__(name, location, wallet)


    def is_in_range(self , vendor):
        if abs(self.location - vendor.location) <= vendor.range:
            return True
        else:
            return False

    def have_enough_mony(self, vendor, number_of_icecreams):
        self.number_of_icecreams = number_of_icecreams
        if self.wallet.money >= (vendor.price * number_of_icecreams):
            return print("You can buy")
        else:
            print("You don't have enough money")

    def request_icecream(self, vendor, number_of_icecream):
        if self.is_in_range(vendor) and self.have_enough_money(vendor, number_of_icecream):
            vendor.sellTo(customer, number_of_icecream)

    def __str__(self):
        return f"Customer {super().__str__}"


customer = Customer("Abdallah", 3, 6)
person = Person("Moh", 5, 50)
vendor = Vendor("Abdallah", 3, 6)