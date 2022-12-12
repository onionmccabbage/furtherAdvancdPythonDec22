# a decorator adds something to what we already have

# here is a decorator function - to be used to decorate other functions
def showArgs(f): # f is the function being decorated
    '''This decorator will reveal any args/kwargs passed in to any function'''
    def newFunct(*args, **kwargs):
        # *args is the tuple of any positional arguments passed in
        # **kwargs is the dictionary of any passed in keyword aruments
        print('Running a function called {}'.format( f.__name__ ))
        print('Positional arguments are {}'.format(args))
        print('Keyword arguments are {}'.format(kwargs))
        return f(*args, **kwargs) # un the decorated function
    return newFunct

# here is a simple function (so we can decorate it)
@showArgs # our showArgs function now becomes a decorator
# be careful - the order of the decorator matters - a decorator appies to the immediately following function
def addIntegers(a, b):
    return a+b

@showArgs # we can decorate ANY function
def raiseToPower(m, n):
    return m**n

if __name__ == '__main__':
    print( addIntegers(1, 2) ) # passed in as positional arguments (0, 1, 2 ...)
    print( addIntegers(a=1, b=2) ) # passed in as keyword arguments
    print( addIntegers(1, b=2) ) # passed in keyword and positional arguments
    print( raiseToPower(10, n=3) )