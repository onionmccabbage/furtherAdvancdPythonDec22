# cProfile is a performant way to profile non-trivial code modules
# invoke cProfile as follows:
# python -m cProfile -o profiling_output using_cProfile.py

# number of calls, total times, time per call, cumulative times

from functools import reduce

def fib(n): # way more performant - under a second for fb(42)
    sequence = (0,1)
    for _ in range(2, n+1):
        sequence += (reduce(lambda a,b: a+b, sequence[-2:]),)
    return sequence[n]

# def fib(n): # much slower - about a minute for 42
#     if n<=1: return n
#     else:
#         return(fib(n-1)+fib(n-2))

def count():
    count.num_calls += 1
    print(count.num_calls)

if __name__ == '__main__':
    count.num_calls = 0
    for _ in range(1,99):
        count()
    f = fib(32)
    print(f)