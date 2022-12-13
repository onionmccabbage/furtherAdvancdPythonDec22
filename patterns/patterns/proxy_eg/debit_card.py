from payment import Payment
from bank import Bank

# the DebitCard is a proxy for the Bank
class DebitCard(Payment):
    def __init__(self):
        self.bank = Bank()
    def do_pay(self):
        card = input('Swipe, Tap or Insert Card? ')
        self.bank.setCard(card)
        # call do_pay on the parent Bank
        return self.bank.do_pay() # True or False