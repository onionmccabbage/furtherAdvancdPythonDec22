from abc import ABCMeta, abstractmethod

class Order(metaclass=ABCMeta):  # we inherit from ABC
    @abstractmethod
    def execute(self):
        pass # we never implement code in the abstract

if __name__ == '__main__':
    pass