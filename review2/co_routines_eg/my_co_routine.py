# co-routines in Python are usually generators

# Python naturaly reates generators for us
even_g = (i for i in range(1,14) if i%2 == 0) # generator which yields the even numbers from 1 to 9
print(type(even_g)) # we have a generator
# we can yield the next value from our generator
print( even_g.__next__() ) # 2
print( even_g.__next__() ) # 4
print( even_g.__next__() ) # 6
# NB the values are never persisted in memory

# we can iterate over a generator
for member in even_g:
    print(member)

# the generator is then exhausted - there are no furhter members to be yielded

# we can define our own custom generator
def tally(inc):
    score = 0
    while True:
        yield score # the 'yield' statement makes this a generator function
        score += inc

if __name__ == '__main__':
    w = tally(5)
    print(type(w)) # w is a generator (a co-routine)
    print( next(w) ) # 0
    print( next(w) ) # 5
    print( next(w) ) # 10
    print( w.__next__() ) # 15
    # we can explicitly close our generator
    w.close() # this will end the infinite loop in tally