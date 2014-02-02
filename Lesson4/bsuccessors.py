# -----------------
# User Instructions
# 
# Write a function, bsuccessors(state), that takes a state as input
# and returns a dictionary of {state:action} pairs.
#
# A state is a (here, there, t) tuple, where here and there are 
# frozensets of people (indicated by their times), and potentially
# the 'light,' t is a number indicating the elapsed time.
#
# An action is a tuple (person1, person2, arrow), where arrow is 
# '->' for here to there or '<-' for there to here. When only one 
# person crosses, person2 will be the same as person one, so the
# action (2, 2, '->') means that the person with a travel time of
# 2 crossed from here to there alone.

def bsuccessors(state):
    """Return a dict of {state:action} pairs. A state is a (here, there, t) tuple,
    where here and there are frozensets of people (indicated by their times) and/or
    the 'light', and t is a number indicating the elapsed time. Action is represented
    as a tuple (person1, person2, arrow), where arrow is '->' for here to there and 
    '<-' for there to here."""
    here, there, t = state
    
    if 'light' in here:
        changed  = here
        symbol   = '->'
        op_here  = frozenset.difference
        op_there = frozenset.union
    else:
        changed  = there
        symbol   = '<-'
        op_here  = frozenset.union
        op_there = frozenset.difference

    dict = {}
    _changed = list({ 'light' } ^ changed) # returns a list without a light
    for i in range(len(_changed)):
        for j in range(i, len(_changed)):
            a, b = _changed[i], _changed[j]
            newset = {a, b, 'light'}
            dict[op_here(here, newset), op_there(there, newset), a + b + t if i != j else a + t] = (a, b, symbol)

    print dict
    return dict

def test():

    assert bsuccessors((frozenset([1, 'light']), frozenset([]), 3)) == {(frozenset([]), frozenset(['light', 1]), 4): (1, 1, '->')}

    assert bsuccessors((frozenset([]), frozenset([2, 'light']), 0)) == {
                (frozenset([2, 'light']), frozenset([]), 2): (2, 2, '<-')}
    
    return 'tests pass'

print test()
