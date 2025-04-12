from abc import ABC, abstractmethod

# Base IceCream class
class IceCream(ABC):
    @abstractmethod
    def get_description(self):
        pass
    
    @abstractmethod
    def cost(self):
        pass

# Concrete IceCream classes
class ChocolateIceCream(IceCream):
    def get_description(self):
        return "Chocolate"
    
    def cost(self):
        return 70

class ButterscotchIceCream(IceCream):
    def get_description(self):
        return "Butterscotch"
    
    def cost(self):
        return 60

# Decorator base class
class IceCreamDecorator(IceCream):
    def __init__(self, ice_cream):
        self.ice_cream = ice_cream
    
    @abstractmethod
    def get_description(self):
        pass
    
    @abstractmethod
    def cost(self):
        pass



# Concrete Decorators
class RainbowSprinklesDecorator(IceCreamDecorator):
    def get_description(self):
        return self.ice_cream.get_description() + " with Rainbow Sprinkles"
    
    def cost(self):
        return self.ice_cream.cost() + 20


class ChocoChipsDecorator(IceCreamDecorator):
    def get_description(self):
        return self.ice_cream.get_description() + " with Choco Chips"
    
    def cost(self):
        return self.ice_cream.cost() + 15


class ChocolateSyrupDecorator(IceCreamDecorator):
    def get_description(self):
        return self.ice_cream.get_description() + " with Chocolate Syrup"
    
    def cost(self):
        return self.ice_cream.cost() + 20



ice_cream1 = ButterscotchIceCream()
ice_cream1 = ChocolateSyrupDecorator(ChocoChipsDecorator(ice_cream1))
print("Desc:", ice_cream1.get_description())
print("Cost:", ice_cream1.cost())
    
ice_cream2 = ChocolateIceCream()
ice_cream2 = RainbowSprinklesDecorator(ChocoChipsDecorator(ice_cream2))
print("Desc:", ice_cream2.get_description())
print("Cost:", ice_cream2.cost())
