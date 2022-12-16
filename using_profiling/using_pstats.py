# we can use pstats to open and read the output of a cProfile result
import pstats

def main():
    p = pstats.Stats('profiling_output')
    p.print_stats()


if __name__ == '__main__':
    main()