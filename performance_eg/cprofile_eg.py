from functools import reduce

from timeit import default_timer

# this one is WAY more performant
def fib0(n):
    sequence = (0,1) # a tuple
    for i in range(n+1):
        sequence += (reduce(lambda a, b: a+b, sequence[-2:]),)
    return sequence[n]

# this one is slower
def fib(n):
    if n<=1:
        return 1
    else:
        return (fib(n-1)+fib(n-2)) # iteratively call the same function

if __name__ == '__main__':
    max_n = 42
    s = default_timer()
    fib(max_n)
    e = default_timer()
    s0 = default_timer()
    fib0(max_n)
    e0 = default_timer()
    # times were: 57.5810612 and 3.129999999629263e-05
    print(f'times were: {e-s} and {e0-s0}')
