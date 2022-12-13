from rx import create 
from rx import operators as op
import random
#here we make an observable that will deliver stateful values over time
def my_observable(observer, scheduler):
    while True:
        r = random.randint(0,100)
        observer.on_next(r)
        if r == 50:
            observer.on_completed()
            break # stop the loop
# make it into an observable then publish it
obs = create(my_observable).pipe(op.publish())

# here are some subscribers to our observable
sub1 = obs.subscribe(on_next = lambda i: print("Subscriber 1 received {0}".format(i)))
sub2 = obs.subscribe(on_next = lambda i: print("Subscriber 2 received {0}".format(i)))
obs.connect()