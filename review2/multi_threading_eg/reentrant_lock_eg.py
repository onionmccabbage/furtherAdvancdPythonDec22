# rlock is a re-entrant lock
# so if a thread has already had access to a lock, it can regain access to that lock
# this is more performant than plain old locks (for multiple lock-release sequences)

import threading
import time
import sys

# this time we will use class threads
class MyWorker():
    def __init__(self):
        self.a = 1
        self.b = 2 # here are some values the threads may need to access
        self.rlock = threading.RLock() # a re-entrant lock
    def modifyA(self):
        with self.rlock: # 'with' will release a lock or rlock when done
            # rlocks know which thread currently 'owns' the rlock
            print(f'RLock acquired: {self.rlock._is_owned()}, modifying "a"')
            self.a += 1
            time.sleep(1) # here the 'with' block ends, so the rlock is released
    def modifyB(self):
        with self.rlock:
            print(f'RLock acquired: {self.rlock._is_owned()}, modifying "b"')
            self.b -= 1
            time.sleep(1)
    def modifyBoth(self):
        self.modifyA()
        self.modifyB()

if __name__ == '__main__':
    worker = MyWorker() # NB tsi is running on the main thread
    worker.modifyA()
    worker.modifyB()
    worker.modifyBoth()
