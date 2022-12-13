# we will need to pip isntall rx
# or conda install rx
import rx # rx is expecially good as obervable streams of asynchronous state changes
# operators include map, filter, sort etc.
from rx import operators as op # convention
# we will need to pip install requests
# or conda install requests
import requests
# we need our utility
from util import filterNames

'''We will consume an API to get asynchronous data about users (this is a stream of data)
   The data comes back eventually (it is asynchronous)
   We will then check for user names beginning with... (i.e. filter the names)
   We can also map the names as needed
'''
def main():
    '''ask the user for a letter'''
    letter = input('Find users starting with which letter? ')
    all_users = requests.get('https://jsonplaceholder.typicode.com/users')
    users = all_users.json() # just read the json into a data structure (our state)
    # print(type(users), users)
    # we now use rx to make an observable out of our stateful data structure
    # we can make an observable from any iterable structure or stream
    users_obs = rx.from_(users) # or from_list - we now have an observable
    # we can respond to our observable
    sub = users_obs.pipe( # pipe will respond to asynchronouse changes to our observable
        # these operators will only operate when the data is ready (async)
        op.filter( lambda c:filterNames(c, letter) ),
        op.map( lambda a:a['name'] ), # just show the name
        # op.do( lambda x:print(x)))
    )
    users.append({'name':'Clare'}) # we can mutate the state of our data source (which we are observing)
    users.append(True) # breaks our observable (True is not subscriptable)
    # we can subscribe to our observable repeatedly
    sub.subscribe(
        # we can implement next, error and complete handlers
        on_next      = lambda i: print(f'Received {i}'), # each step is COMMA SEPARATED
        on_error     = lambda e: print(f'Received error {e}'),
        on_completed = lambda: print('all done') # nice to be able to tidy up ( ONLY IF NO ERRORS!!! )
    )
    # sub.unsubscribe() # no longer respond to changes in the observable state

if __name__ == '__main__':
    main()

