def leading_substrings(s):
    '''Takes string s as input and returns a list of all 
    the substrings that start from the beginning.
    E.g., leading_substrings('bear') will return 
    ['b', 'be', 'bea', 'bear'].'''
    return [s[:i+1] for i in range(len(s))]