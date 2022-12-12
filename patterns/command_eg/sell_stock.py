from order import Order

class SellStock(Order): # a concrete class inheriting from our abstract class
    def __init__(self, stock):
        self.stock = stock
    @property # usually the 'getter' method comes first
    def stock(self):
        return self.__stock
    @stock.setter # the nthe 'setter' method for a property
    def stock(self, new_stock):
        if type(new_stock) == str and new_stock != '':
            self.__stock = new_stock
        else:
            self.__stock = 'Ericsson'
    # we are obliged to implement the 'execute' method from the abstract class
    def execute(self):
        return self.stock.sell() # this will only work when we have actual stock with actual 'buy' methods

if __name__ == '__main__':
    # exercise the code
    b = BuyStock('Galway')
    print( f'You bought {b.stock()}' )