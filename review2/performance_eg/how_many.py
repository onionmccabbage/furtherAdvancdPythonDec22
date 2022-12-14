import multiprocessing
# NB threads all run on the SAME cpu, sharing the same Python instance
# processes can run on SEPARATE cpus, with their own copy of Python
num_proc = multiprocessing.cpu_count()

# we would use threading for concurrent work such as sockets, microservices, image processing
# we would use multiprocessing for e.g a web server with totally independent users

print(f'currently running on a machine with {num_proc} processors')