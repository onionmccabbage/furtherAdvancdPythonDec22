# the green event (gevent) was an early success in making threads run independently
# legacy code may still use gevent for efficient threading
import gevent
from gevent import socket # we need the socket from gevent

def demo():
    hosts = ['www.ericsson.com', 'www.bbc.co.uk', 'swapi.dev', 'www.python.org']
    # we can get a list of the IP addresses of these hosts
    jobs  = [gevent.spawn(socket.gethostbyname, host) for host in hosts]
    # we need to join the threads
    gevent.joinall(jobs, timeout=6)
    for job in jobs:
        print(job.value)

if __name__ == '__main__':
    demo()