from abc import ABC, abstractmethod


class Mobile(ABC):
    @abstractmethod
    def create_mobile(self):
        pass


# IPhone class
class IPhone(Mobile):
    def create_mobile(self):
        print("Creating IPhone Mobile Phone")


# OnePlusPhone class
class OnePlusPhone(Mobile):
    def create_mobile(self):
        print("Creating One Plus Mobile Phone")


# RealMe class
class RealMe(Mobile):
    def create_mobile(self):
        print("Creating RealMe Mobile Phone")


# Factory class
class MobileFactory:
    def create_mobile(self, company_name):
        if not company_name:
            return None
        company_name = company_name.upper()
        if company_name == "IPHONE":
            return IPhone()
        elif company_name == "ONEPLUS":
            return OnePlusPhone()
        elif company_name == "REALME":
            return RealMe()
        else:
            return None


factory = MobileFactory()

mobile = factory.create_mobile("IPHONE")
mobile.create_mobile()

mobile = factory.create_mobile("ONEPLUS")
mobile.create_mobile()

mobile = factory.create_mobile("REALME")
mobile.create_mobile()
