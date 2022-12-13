from order import Order

class BuyStock(Order): # a concrete class inheriting from our abstract class
    def __init__(self, stock):
        self.stock = stock # this will call the __stock setter
    @property # usually the 'getter' method comes first
    def stock(self): # make this function appear as a property
        return self.__stock # name-mangled proerty (a bit like 'internal')
    @stock.setter # then the 'setter' method for a property
    def stock(self, new_stock):
        if new_stock != '':
            self.__stock = new_stock
        else:
            raise Exception('problem with stock')
    # we are obliged to implement the 'execute' method from the abstract class
    def execute(self):
        return self.stock.buy() # this will only work when we have actual stock with actual 'buy' methods

if __name__ == '__main__':
    # exercise the code
    b = BuyStock(order)
    print( f'You bought {b.stock()}' )