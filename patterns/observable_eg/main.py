# the Observer pattern uses a publish-subscribe model
# the publisher does not need to know what the subscribers will do with the publication

# here is our broadcaster - our publisher, our observable
from news_pub import NewsPublisher

# here are the subscribers, the listeners, the observers
from print_sub import PrintSubscriber
from email_sub import EmailSubscriber
from media_sub import MediaSubscriber

def main():
    pass

if __name__ == '__main__':
    main()

