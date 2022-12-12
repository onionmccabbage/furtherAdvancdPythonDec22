class Agent():
    def __init__(self):
        self.__orderQueue = [] # start with an empty list
    def placeOrder(self, order):
        self.__orderQueue.append(order)
        order.execute() # we may need to wait for resources to became available

if __name__ == '__main__':
    pass