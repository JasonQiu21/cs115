'''
Created on 2021-10-12
@author:   Jason Qiu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 5 
'''
d = {}
def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    if n in d:
        pass
    elif n == 0:
        d[n] = 2
    elif n == 1:
        d[n] = 1
    else:
        d[n] = fast_lucas(n-1) + fast_lucas(n-2)
    return d[n]
d2 = {}
def fast_change(a: int, coins = [1,5,10,25,50]):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    if a in d2:
        pass
    else:
        d2[a] = {}
    if coins == []:
        return float('inf')
    elif coins[-1] in d2[a]:
        pass
    elif a == coins[-1]:
        d2[a][coins[-1]] = 1
    elif a < coins[-1]:
        d2[a][coins[-1]] = fast_change(a, coins[:-1])
    else:
        use_it = 1 + fast_change(a-coins[-1], coins)
        lose_it = fast_change(a, coins[:-1])
        d2[a][coins[-1]] = min(use_it, lose_it)
    return d2[a][coins[-1]]


# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))