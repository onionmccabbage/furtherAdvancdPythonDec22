# 'timeit' is a more accurate timer than 'time'
from timeit import default_timer
# 'time' is not as accurate as 'timeit'
from time import time

# NB when profiling or timing its a good idea to ake several iterations and find the average

# here is a reasonably complex function
def fib(n):
    if n<=1:
        return 1
    else:
        return (fib(n-1)+fib(n-2)) # iteratively call the same function

if __name__ == '__main__':
    # measure how long this takes
    start_a = time() # we imported time from the time library
    start_b = default_timer() # this comes from the timeit library
    r = fib(42) # be careful!!!
    end_a = time()
    end_b = default_timer()

    # see how long it took
    # timeit can ignore non-python items
    print(f'Timeit says the operation took {end_b-start_b}')
    # time simply takes the total time, regardless of what occupied the time
    print(f'Time says the operation took {end_a-start_a}')

    print(r)