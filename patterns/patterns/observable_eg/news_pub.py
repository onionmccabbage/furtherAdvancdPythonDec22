# we will declare an observable (publisher)
class NewsPublisher():
    def __init__(self):
        self.__subscribers = [] # start with an empty list
        self.latest_news = None
    def attach(self, new_sub):
        self.__subscribers.append(new_sub)
    def detach(self):
        self.__subscribers.pop() # just remove the most recent subscription
    def iter_subscribers(self): # iterate over all the current subscribers
        return [type(x).__name__ for x in self.__subscribers]
    def notify_subscribers(self):
        for sub in self.__subscribers:
            sub.update() # call the update method of each subscriber
    # we need to be able to add news items
    def add_news(self, news):
        self.__latest_news = news
    def get_news(self):
        return f'News: {self.__latest_news}'