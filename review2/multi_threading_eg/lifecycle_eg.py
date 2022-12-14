# so far everythnig has been running on the main thread
# we can start additional threads to run at the same time
import time
import random
import threading # this library lets us create Threads

def threadWorker():
    print('Thread is running') # every thread has a lifecycle
    time.sleep(0.5) # sleep for half a second
    print('Thread is terminating')

def executeThread(i): 
    print(f'Thread {i} has started')
    time.sleep( random.randint(1, 2) )
    print(f'Thread {i} is terminating')

if __name__ == '__main__':
    myThread = threading.Thread(target=threadWorker)
    myThread.start()
    myThread.join() #  join the other thread back to this main thread
    # we can handle as many threads as we like
    for i in range(0, 10): # 0 to 9
        thread = threading.Thread(target=executeThread, args=(i,)) # we pass positional args as a tuple
        thread.start()
        # we can see the active threads like this
        print(f'Active threads: {threading.enumerate()}')