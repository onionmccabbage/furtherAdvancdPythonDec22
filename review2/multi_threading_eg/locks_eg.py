# threads share the SAME processor, the SAME instance of Python and the SAME data-access members
# e.g. shared DB, API,file i/o etc.
# we need to lock resources for exclusive access
# NB try this code without locks - A and B battle over the value of the counter!!!

import threading

counter = 0 # this is a global asset - could be a db, api etc.

lock = threading.Lock()

def workerA():
    global counter # we now have access to the global variable called 'counter'
    lock.acquire() # this function now has exclusive use of the lock
    try:
        while counter < 20:
            counter += 1 # increment the global counter
            print(f'Worker A increments the counter to {counter}')
    except Exception as e:
        print(f'Something went wrong {e}')
    finally:
        lock.release() # we no longer have exlusive access to the locked resource

def workerB():
    global counter # we now have access to the global variable called 'counter'
    lock.acquire() # this function now has exclusive use of the lock
    try:
        while counter > -20:
            counter -= 1 # deccrement the global counter
            print(f'Worker B decrements the counter to {counter}')
    except Exception as e:
        print(f'Something went wrong {e}')
    finally:
        lock.release() # we no longer have exlusive access to the locked resource

if __name__ == '__main__':
    t1 = threading.Thread(target=workerA)
    t2 = threading.Thread(target=workerB)
    t1.start()
    t2.start()
    t1.join() # at the earliest possible point, we ask the thread to rejoin the main thread
    t2.join()