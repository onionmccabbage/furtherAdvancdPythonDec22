# we will need to pip isntall rx
# or conda install rx
import rx # rx is expecially good as obervable streams of asynchronous state changes
# operators include map, filter, sort etc.
from rx import operators as op # convention
# we will need to pip install requests
# or conda install requests
import requests

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
    users_obs = rx.from_(all_users) # or from_list - we now have an observable
    # we can respond to our observable
    sub = users_obs.pipe( # pipe will respond to asynchronouse changes to our observable
        # these operators will only operate when the data is ready (async)
        op.filter(  )
    )

if __name__ == '__main__':
    main()

