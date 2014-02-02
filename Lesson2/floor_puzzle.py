#------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on 
# different floors of a five-floor apartment building. 
#
# Hopper does not live on the top floor. 
# Kay does not live on the bottom floor. 
# Liskov does not live on either the top or the bottom floor. 
# Perlis lives on a higher floor than does Kay. 
# Ritchie does not live on a floor adjacent to Liskov's. 
# Liskov does not live on a floor adjacent to Kay's. 
# 
# Where does everyone live?  
# 
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay, 
# Liskov, Perlis, and Ritchie.

import itertools

def floor_puzzle():
    ppls = {'Hopper': 0, 'Kay': 1, 'Liskov': 2, 'Perlis': 3, 'Ritchie': 4}
    floors = [1, 2, 3, 4, 5]
        
    g = (perm for perm in itertools.permutations(floors)
         if perm[ppls['Hopper']] != 5 # top floor
         if perm[ppls['Kay']] != 1 # bottom floor
         if perm[ppls['Liskov']] != 5 
         if perm[ppls['Liskov']] != 1
         if perm[ppls['Perlis']] > perm[ppls['Kay']] # Perlis lives higher than Kay
         if abs(perm[ppls['Ritchie']] - perm[ppls['Liskov']]) != 1 # floors are not adjacent
         if abs(perm[ppls['Liskov']] - perm[ppls['Kay']]) != 1)
        
    return next(g)

print floor_puzzle()
