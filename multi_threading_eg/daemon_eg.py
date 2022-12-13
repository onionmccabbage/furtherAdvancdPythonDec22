from threading import Thread
import time
def standardThread():
    print('starting standard thread')
    time.sleep(5)
    print('ending standard thread')

def daemonThread():
    while True: # careful  -this is an endless loop
        print('heartbeat....')
        time.sleep(0.25)

if __name__ == '__main__':
    s = Thread(target=standardThread)
    d = Thread(target=daemonThread)
    d.setDaemon(True) # we now have a daemon thread - it will terminate whne the other threads are done
    s.start()
    d.start()