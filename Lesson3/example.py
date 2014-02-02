def lit(s):         return lambda Ns: set([s]) if len(s) in Ns else null
def alt(x, y):      return lambda Ns: x(Ns) | y(Ns)# your code here
def star(x):        return lambda Ns: opt(plus(x))(Ns)
def plus(x):        return lambda Ns: genseq(x, star(x), Ns) #Tricky
def oneof(chars):   return lambda Ns: set(chars) if 1 in Ns else null# your code here
def seq(x, y):      return lambda Ns: genseq(x, y, Ns)
def opt(x):         return alt(epsilon, x)
dot = oneof('?')    # You could expand the alphabet to more chars.
epsilon = lit('')   # The pattern that matches the empty string.</p>

null = frozenset([])

def genseq(x, y, Ns):
    Nss = range(max(Ns) + 1)
    return set(m1 + m2 for m1 in x(Nss) for m2 in y(Nss) if len(m1 + m2) in Ns)

# k = plus(lit('a'))
# print k(set([1]))

def n_ary(f):
    """Given binary function f(x, y), return an n_ary function such
    that f(x, y, z) = f(x, f(y,z)), etc. Also allow f(x) = x."""
    def n_ary_f(x, *args):
        if len(args) < 2: f(x, args[0])
        else: f(x, n_ary(f)(args[0], *args[1:]))
        
    return n_ary_f
