# facade simply means a wall or a surface
# we use a facade to provide a single point of access to several disparate subsystems
# in this example we need a coder, a tester, a technician, an artisan and a manager
# they are all non-interdependant classes
class Coder():
    def __init__(self):
        print('write some code') # or do something more complex
    def __is_available__(self):
        print('coding skills are available') # we might use checks to determine availablity
        return True # or False
    def book_time(self):
        if self.__is_available__():
            print('coder has been booked')

class Tester():
    def __init__(self):
        print('preparing tests')
    def testing(self):
        print('tests are in place')

class Technician():
    def __init__(self):
        print('preparing equipment for the team')
    def do_stuff(self):
        print('network, machines and stuff are in place')

class Artisan():
    def __init__(self):
        print('designing things...')
    def make_prototype(self):
        print('wireframes are ready')
        
# a manager can provide a facade to access the assets
class Manager():
    def __init__(self):
        print('Manager says I can arrange the team')
    def arrange(self):
        # the facade will provide instances of all the subsystems/microservices
        self.coder = Coder()
        self.tester = Tester()
        self.technician = Technician()
        self.artisan = Artisan()
        # put them to work
        self.coder.book_time()
        self.tester.testing()
        self.technician.do_stuff()
        self.artisan.make_prototype()
        # we could easily pass parameters between the assets

# a client needs to make use of our assets (via the manager facade)
class Client():
    def __init__(self):
        print('we need a team...')
    def ask_manager(self):
        print('lets ask the manager')
        m = Manager() # we now have access to our facade
        m.arrange()   # ... the facade deals with all the subsystems
    def __del__(self): # all classes will run __del__ when they finish
        print('all done')

if __name__ == '__main__':
    import time
    s= time.time()
    customer = Client()
    customer.ask_manager() # get things going...
    e = time.time()
    # print the time