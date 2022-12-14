# we can write a class which inherits from Processing
import multiprocessing
import os
import time
# the 'Self' library is really handy to access the operating system
from typing_extensions import Self
from memory_profiler import profile

# remember Process is a process-access-object
class MyProcess(multiprocessing.Process):
    def __init__(self):
        super(MyProcess, self).__init__()
    # we override the default 'run' method of 'Process'
    def run(self):
        time.sleep(2)
        print(f'Child process ID is {multiprocessing.current_process().pid}')

@profile
def main():
    procs = []
    # remember we also have a main process
    # range is 0 to num-1. Here 0-15. 
    for i in range(os.cpu_count()-1): # no point having more processes than processors
        p = MyProcess() # this will call the 'run' method
        p.start()
        procs.append(p)
    # good practice to join the processes
    for p in procs:
        p.join()


if __name__ == '__main__':
    main()
