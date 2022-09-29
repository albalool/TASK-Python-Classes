from turtle import distance
from typing_extensions import Self


class Wallet:
    def __init__(self, money):
        self.money = money

    def credit(self, amount):
        self.money += amount
        print(f"Your money {self.money} ")
        

    def debit(self, amount):
        self.money -= amount
        print(f"Your money {self.money} ")
    
    def __str__ (self):
        return f"{self.money}"


wallet = Wallet(6)
wallet = Wallet()  # This should default money inside the wallet to 0
print(wallet.money)


class Person:
    def __init__(self, name, location, money):
        self.name = name
        self.location = location
        self.wallet = Wallet(money)
    
    location = 8

    def moveTo(self, point):
        self.location = self.location - point

    def __str__ (self):
        return f"Hi I'm {self.name}, and my location is {self.location} I have {self.wallet} in my bank"



person = Person("Moh", 5, 50)
print(person)
 


class Vendor(Person):
    def __init__(self, name, location, money, range , price):
        super().__init__(name, location, money)
        self.range = range
        self.price = price
    range = 5
    price = 1

    def sellTo(customer, number_of_icecreams):
        Person.moveTo()
        Wallet.debit()


vendor = Vendor("Abdallah", 3, 6)


class Customer(Person):
    def __init__(self, name, location, money):
        super().__init__(name, location, money)


    def is_in_range():
        distance = abs(Vendor(range) - Person.location())
        return distance

    def have_enough_mony(vendor, number_of_icecreams):
        if Vendor.money() >= number_of_icecreams:
            return print("You can buy")
        else:
            print("You don't have enough money")

    def request_icecream(vendor, number_of_icecream):
        if
        else:
            pass


customer = Customer("Abdallah", 3, 6)
