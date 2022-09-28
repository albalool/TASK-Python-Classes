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


#wallet = Wallet(6)
# # wallet = Wallet()  # This should default money inside the wallet to 0
#print(wallet.money)
# wallet.credit(9)
# wallet.debit(5)


class Person:
    def __init__(self, name, location, money):
        self.name = name
        self.location = location
        self.wallet = Wallet(money)

  
    def moveTo(self, point):
        self.location = self.location - point

    def __str__ (self):
        return f"Hi I'm {self.name}, and my location is {self.location} I have {self.wallet} in my bank"



person = Person("Moh", 5, 50)
print(person)



# class Vendor:
#     # implement Vendor!
#     pass


# vendor = Vendor("Abdallah", 3, 6)


# class Customer:
#     # implement Customer!
#     pass


# customer = Customer("Abdallah", 3, 6)
