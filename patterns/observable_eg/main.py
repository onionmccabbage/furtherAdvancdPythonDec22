# the Observer pattern uses a publish-subscribe model
# the publisher does not need to know what the subscribers will do with the publication

# here is our broadcaster - our publisher, our observable
from news_pub import NewsPublisher

# here are the subscribers, the listeners, the observers
from print_sub import PrintSubscriber
from email_sub import EmailSubscriber
from media_sub import MediaSubscriber
from other_sub import OtherSubscriber

# a tuple of subscribers
subs = (MediaSubscriber, PrintSubscriber, EmailSubscriber, OtherSubscriber)

def main():
    news_publisher = NewsPublisher()
    # iterate over each subscriber, notifying of fresh news
    for Subscriber in subs:
        Subscriber(news_publisher) # we will end up with three subscribers
        news_publisher.add_news('News flash: its nearly done...')
    news_publisher.notify_subscribers() # they all get 'push' notification

if __name__ == '__main__':
    main()

