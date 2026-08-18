# ----Abstraction--------

from abc import ABC, abstractclassmethod

class Payment(ABC):

    @abstractclassmethod
    def process_payment(self,amount):
        pass


# Child class 1
class CreditCardPayment(Payment):

    def process_payment(self, amount):
        print("Processing credit card payment of", amount)


# Child class 2
class UPIPayment(Payment):

    def process_payment(self, amount):
        print("Processing UPI payment of ₹", amount)


# Creating objects
credit_card = CreditCardPayment()
upi = UPIPayment()


# Calling methods
credit_card.process_payment(5000)
upi.process_payment(2500)         
