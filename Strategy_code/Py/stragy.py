from abc import ABC, abstractmethod

# Define the interface
class DiscountStrategy(ABC):
    @abstractmethod
    def give_discount(self, amount):
        pass


# Implement different discount strategies
class CashbackDiscount(DiscountStrategy):
    def give_discount(self, amount):
        return amount * 0.10 


class CouponDiscount(DiscountStrategy):
    def give_discount(self, amount):
        return amount * 0.15  


class FlatDiscount(DiscountStrategy):
    def give_discount(self, amount):
        return amount * 0.20  


# Context class to apply discounts
class ApplyDiscount:
    def __init__(self, discount_strategy: DiscountStrategy):
        self.discount_strategy = discount_strategy

    def get_discount(self, amount):
        return self.discount_strategy.give_discount(amount)

    def set_strategy(self, discount_strategy: DiscountStrategy):
        self.discount_strategy = discount_strategy


# Example usage
print("Customer1:")
amount = 1000  # Example amount in TK
customer1 = ApplyDiscount(FlatDiscount())

discount1 = customer1.get_discount(amount)
print(f"Flat discount: {discount1} TK after 20%")

customer1.set_strategy(CashbackDiscount())
discount2 = customer1.get_discount(amount)
print(f"Cashback discount: {discount2} TK after 10%")


print("\nCustomer2:")
amount2 = 2000  # Example amount in TK
customer2 = ApplyDiscount(FlatDiscount())

discount3 = customer2.get_discount(amount2)
print(f"Flat discount: {discount3} TK after 20%")

customer2.set_strategy(CouponDiscount())
discount4 = customer2.get_discount(amount2)
print(f"Coupon discount: {discount4} TK after 15%")












#cfdef3