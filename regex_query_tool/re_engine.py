import re

def find(pattern, sequence):
    '''
    Function to find all the matched sequences in the provided data 
    as per pattern.
    '''
    compiled = re.compile(pattern)
    result = compiled.findall(sequence)
    return result

def replace(pattern, repl, sequence):
    '''
    Function to replace the matched data with the supplied data.
    '''
    compiled = re.compile(pattern)
    result = compiled.sub(repl, sequence)
    return result

if __name__ == "__main__":
    pass