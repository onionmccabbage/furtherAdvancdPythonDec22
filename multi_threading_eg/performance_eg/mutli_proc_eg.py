import multiprocessing
import os
def do_this(what):
    whoami(what)

# every Python module will always run on one processor in at least ONE thread (the main thread)

def whoami(what):
    print(f'Process {os.getpid()} says {what}')

if __name__ == '__main__':
    whoami('I am the main program')
    # run some fresh processes
    procs = []
    # what if we try more than cpu.count() - the os will multi-task
    # we end up with some sequential operation
    for n in range(os.cpu_count()-1): 
        p = multiprocessing.Process(target=do_this, args=(f'function {n}',))
        procs.append(p)
        p.start() # dont forget to start the process!!!!
    for p in procs:
        # join means return operation to the main thead, including any termination flag
        p.join() # good idea to join the process at the earliest opportunity
