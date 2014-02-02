# --------------
# User Instructions
#
# Write a function, inverse, which takes as input a monotonically
# increasing (always increasing) function that is defined on the 
# non-negative numbers. The runtime of your program should be 
# proportional to the LOGARITHM of the input. You may want to 
# do some research into binary search and Newton's method to 
# help you out.
#
# This function should return another function which computes the
# inverse of the input function. 
#
# Your inverse function should also take an optional parameter, 
# delta, as input so that the computed value of the inverse will
# be within delta of the true value.

# -------------
# Grading Notes
#
# Your function will be called with three test cases. The 
# input numbers will be large enough that your submission
# will only terminate in the allotted time if it is 
# efficient enough. 

def slow_inverse(f, delta=1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def f_1(y):
        x = 0
        while f(x) < y:
            x += delta
        # Now x is too big, x-delta is too small; pick the closest to y
        return x if (f(x)-y < y-f(x-delta)) else x-delta
    return f_1 

def inverse(f, delta = 1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    delta = delta / 2.
    count = 0
    def inverse(y):
        count = 0
        low = 0
        high = 1000
        while not (f(high) > y): high += 1000

        mid = low + (high - low) / 2.
        while not((f(mid) > (y - delta)) and (f(mid) < (y + delta))):
            print 'count %s: low = %s, mid = %s, high = %s' % (str(count), low, mid, high)
            if f(mid) > y: high = mid
            else: low = mid
            mid = low + (high - low) / 2.
            count += 1
        return mid

    return inverse
    
def square(x): return x*x
sqrt = inverse(square, 1/12800000.)

#print sqrt(1000000000)
print sqrt(100)
