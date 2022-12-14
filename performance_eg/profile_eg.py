from memory_profiler import profile
import collections

# we can decorate ANY function with profile
@profile
def someFn():
    my_deq = collections.deque('98765432')
    my_deq.append('1') # appends to the right end of the queue
    print(f'Deque {my_deq}')
    my_deq.appendleft('0')
    print(f'Deque {my_deq}')
    my_deq.pop() # remove from the right
    print(f'Deque {my_deq}')
    my_deq.popleft()
    print(f'Deque {my_deq}')
    # try to make use of a lot of memory
    for i in range(1024**2):
        my_deq.append(str(i)) # use a generator instead - then the values do not need to persist in memory

def main():
    someFn()

if __name__ == '__main__':
    main()