# import the other classes
from stock_trade import StockTrade
from agent import Agent
from buy_stock import BuyStock
from sell_stock import SellStock

def main():
    stock = StockTrade()
    buy   = BuyStock(stock)
    sell  = SellStock(stock)
    agent = Agent()
    # invoke the commands
    agent.placeOrder(buy)
    agent.placeOrder(sell)

if __name__ == '__main__':
    main()