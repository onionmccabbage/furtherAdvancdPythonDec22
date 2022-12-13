from payment import Payment
import random

class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None
    def setCard(self, card):
        self.card = card
    def __getAccount(self): # the __ makes this 'internal'
        self.account = self.card
        return self.account
    def __has_funds(self):
        print(f'Bank is checking if {self.__getAccount()} has funds')
        # randomly decide if there are funds
        return bool(random.getrandbits(1)) # True or False
    def do_pay(self):
        if self.__has_funds():
            print('Bank is paying')
            return True
        else:
            print('insufficient funds')
            return False