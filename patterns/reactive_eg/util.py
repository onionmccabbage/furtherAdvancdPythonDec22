# here is a utility function that will filter names by first letter
def filterNames(struct, letter):
    if struct['name'].startswith(letter):
        return struct['name'] # we have a match, so return this item
    else:
        return '' # no match

if __name__ == '__main__':
    structure = {'name':'Timnit'}
    structure = {'name':'Grace'}
    structure = {'name':'Ada'}
    print( filterNames(structure, 'A') )