# we can read in the profile output file to see the results
import pstats

def main():
    #read in the output file
    p = pstats.Stats('profiling_output')
    # print the results
    p.print_stats()

# NB make sure to run this module locally, e.g. in a command window
if __name__ == '__main__':
    main()