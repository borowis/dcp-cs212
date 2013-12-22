# -----------
# User Instructions
# 
# Define a function, kind(n, ranks).

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    print
    print 'N is ' + str(n) + ', ranks are ' + str(ranks)
    i = 0
    while i < len(ranks):
        count = 0
        print 'Computing for ' + str(ranks[i])
        for j in range(i, len(ranks)):
            print '(' + str(ranks[j]) + ', ' + str(ranks[i]) + ')',
            if ranks[j] == ranks[i]:
                count += 1
            else:
                break
        print
        print 'Count is ' + str(count)
        print 'i is ' + str(i) + ', j is ' + str(j)
        if count == n:
            print 'Returning ' + str(ranks[i])
            return ranks[i]
        if len(ranks) - j < n:
            return None
        i = j
        print 'i is now ' + str(i)
        print
    
def test():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    fkranks = card_ranks(fk)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    return 'tests pass'
    
def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return ranks

print test()
