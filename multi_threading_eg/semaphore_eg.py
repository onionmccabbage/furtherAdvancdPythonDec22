# semaphores let us specify the maximum number of concurrent threads accessing a resource
# in this example, a finite number of tickets wil be available
# the tickets will be distributed between ticket sellers (on deparate threads)
# the semaphore will control which thread gets access to the next available tickets to sell

import random
import sys
import time
import threading

# here is a global variable
ticketsAvailable = 100 # try 100

# this class inherits from the Thread class - it is a thread acces class
class TicketSeller(threading.Thread):
    ticketsSold = 0
    # we can pass in a a semaphore
    def __init__(self, sem):
        threading.Thread.__init__(self)
        # super.__init__(self) # aternative syntax - behaves the same
        self.__sem = sem # we have a semaphore for our threads to use
    # because we inherit from Thread, we can override the 'run' method
    def run(self):
        global ticketsAvailable
        # keep selling tickets until we run out!
        running = True
        while running:
            self.__sem.acquire() # like acquiring a lock or rlock, but with multiple concurrent access
            self.randomDelay() # sleep for a random time
            if ticketsAvailable <= 0:
                running = False
            else:
                self.ticketsSold += 1
                ticketsAvailable -= 1
            # dummyFn() # this is a call OUTSIDE the current code bloxk - we need to access he interpreter, so the GIL is invoked
            self.__sem.release() # we must release the semaphore when we no longer need it
            time.sleep(0.01) # delay the thread
        # lets see how many tickets this thread sold
        print(f'Ticket seller {self.getName()} sold {self.ticketsSold} tickets')
    def randomDelay(self):
        time.sleep(random.randint(0,4)/16) # 0, 0.25, 0.5, 0.75 seconds

def dummyFn():
    x = 1
    # print('nothing to see here')


def main():
    sem = threading.Semaphore(2) # how many concurrent threads will be permitted
    sellers = []
    for i in range(0, 4): # more threads than the semaphore allows
        # if a class descends from thread, the 'run' method is automatically invoked when we start it
        seller = TicketSeller(sem) # we have a thread, with access to the semaphore
        sellers.append(seller)
        seller.start()
    # once all the threads are started, we should 'join()' them
    for seller in sellers:
        seller.join()

if __name__ == '__main__':
    main()
