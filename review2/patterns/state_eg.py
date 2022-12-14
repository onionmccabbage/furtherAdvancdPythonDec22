# state is just the data we pass around
# we consider the state to change when variables or data structures are mutated
# we can react to changes of state

# in some cases, state changes are only permitted between certain values
# A laptop can go from 'off' to 'on' but not from 'off' to 'sleep'
# ( we can go from 'on' to 'sleep' )

class ComputerState():
    name = 'state'
    allowed = [] # this list will contain the permitted states
    def switch(self, state):
        if state.name in self.allowed:
            print(f'Current state {self} switching to {state.name}')
            self.__class__ = state # make the state change
        else:
            print(f'Current state {self} cannot switch to {state.name}')
    def __str__(self):
        return self.name

class On(ComputerState):
    name = 'on'
    allowed = ['off', 'sleep', 'hybernate']

class Off(ComputerState):
    name = 'off'
    allowed = ['on']

class Sleep(ComputerState):
    name = 'sleep'
    allowed = ['on']

class Hybernate(ComputerState):
    name = 'hybernate'
    allowed = ['on']

class Computer():
    def __init__(self, model):
        self.model = model # we can have additional data modelling
        self.state = Off() # set an initial state to the Off() class
    def change(self, change_to):
        self.state.switch(change_to)

def main():
    comp = Computer('some model data') # initially the computer will be off
    comp.change(On)
    comp.change(Off)
    comp.change(On)
    comp.change(Sleep)
    comp.change(On)
    comp.change(Hybernate)
    comp.change(On)
    comp.change(Off)
    comp.change(Hybernate)

if __name__ == '__main__':
    main()