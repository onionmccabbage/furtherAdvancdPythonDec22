# why do we use patterns in code? They are like traditions - a known solution to a problem
# and why the 'factory' pattern? Useful solution to creational techniques

# here we need a simple solution to manufacture several types of creature
from abc import abstractmethod # the abc library is 'abstract base class'

# here is a top-level abstract class
class Animal(): # we would have several abstract methods (what we need to do)
    @abstractmethod # this is a decorator, provided by the abc library
    def make_a_noise(self):
        pass # because this is an abstract method, we do not implement the body

# here are some concrete classes we could instantiate
class Dog(Animal): # we implement hte abstract methods here
    def make_a_noise(self): # here we do implement the body of the method
        print('Woof')
class Cat(Animal):
    def make_a_noise(self): 
        print('Miaow')
class Bat(Animal):
    def make_a_noise(self):
        print('_____')
class Lion(Animal):
    def make_a_noise(self):
        print('Roar')

# a factory to create animals
class CreatureFactory(): # NB by convention we Capitalize class names
    def make_sound(self, object_type): # we could assemble a bunch of outcomes for each type
        # eval will evaluate which class was passed in, Note the brackets
        return eval(object_type)().make_a_noise() # this returns a call to a method of an instance

if __name__ == '__main__':
    # here we can exercise the code
    cf = CreatureFactory() # we now have an instance of our factory
    creature = input('which creature? ') # we really should validate this!!!
    cf.make_sound(creature)