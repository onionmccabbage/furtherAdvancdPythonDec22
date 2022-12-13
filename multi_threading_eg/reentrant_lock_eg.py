# rlock is a re-entrant lock
# so if a thread has already had access to a lock, it can regain access to that lock
# this is more performant than plain old locks

import threading
import time
import sys
# this time we will use class threads
class MyWorker():
    pass

if __name__ == '__main__':
    pass