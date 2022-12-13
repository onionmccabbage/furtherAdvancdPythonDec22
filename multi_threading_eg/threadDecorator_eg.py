# we can create a decorator which can be applied to any function to make that function lock safe
# i.e. threaded or not threaded, we can decorate ANY function to be safe when using shared resources

# declare a custom decorator
def lock_a_method(meth):
    if getattr(meth, '__is_locked', False):
        pass
    def locked_method(self, *args, **kwargs):
        with self.__lock: # 'with' will release the lock when done
            return meth(self, *args, **kwargs)
    lock_a_method.__name__ = f'Locked method {meth.__name__}'
    locked_method.__is_locked = True
    return locked_method


if __name__ == '__main__':
    pass


