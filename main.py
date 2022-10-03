class Wallet:
    def __init__(self, money):
        self.money = money

    def credit(self, amount):
        self.money += amount

    def debit(self, amount):
        self.money -= amount


wallet = Wallet(6)


class Person:
    def __init__(self, name, location, money):
        self.name = name
        self.location = location
        self.wallet = Wallet(money)

    def moveTo(self, point):
        self.location = point


person = Person("Nora", 5, 50)


class Vendor(Person):
    def __init__(self, name, location, money):
        super().__init__(name, location, money)
        self.range = 5
        self.price = 1

    def sellTo(self, customer, number_of_icecreams):
        self.location = customer.location
        self.wallet.credit(self.price * number_of_icecreams)
        customer.wallet.debit(self.price * number_of_icecreams)


class Customer(Person):
    def __init__(self, name, location, money):
        super().__init__(name, location, money)

    def _is_in_range(self, vendor):
        x = abs(vendor.location - self.location)
        if x >= vendor.range:
            return True
        else:
            return False

    def _have_enough_mony(self, vendor, number_of_icecreams):
        if self.wallet.money >= (vendor.price * number_of_icecreams):
            return True
        else:
            return False

    def request_icecream(self, vendor, number_of_icecream):
        if self._is_in_range(vendor) and self._have_enough_money(
            vendor, number_of_icecream
        ):
            return vendor.sellTo(self, number_of_icecream)


vendor_lulu = Vendor("lulu", 10, 10)
nearbyCustomer = Customer("Lateefa", 11, 10)
distantCustomer = Customer("Abbas", 1000, 1000)
brokeCustomer = Customer("Aziz", 12, 0)


nearbyCustomer.request_icecream(vendor_lulu, 10)
print(nearbyCustomer.wallet.money)
print(vendor_lulu.wallet.money)
print(vendor_lulu.location)

distantCustomer.request_icecream(vendor_lulu, 10)
print(distantCustomer.wallet.money)
print(vendor_lulu.wallet.money)
print(vendor_lulu.location)

brokeCustomer.request_icecream(vendor_lulu, 1)
print(brokeCustomer.wallet.money)
print(vendor_lulu.wallet.money)
print(vendor_lulu.location)
