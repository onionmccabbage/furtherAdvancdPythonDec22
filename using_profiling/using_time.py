import time # use time.time or time.clock (py2)
from timeit import default_timer # much more platform independent

# declare a reasonably complex function
def fib(n):
    if n<=1: return n
    else:
        return(fib(n-1)+fib(n-2))

if __name__ == '__main__':
    # start = time.time()
    start = default_timer()
    # start2 = time.clock() # python 2 has 'clock()'
    fib(42) # takes about a minute
    # end = time.time()
    end = default_timer()
    # how long ?
    print(end-start)