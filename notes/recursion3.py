# Notes 2021-10-04
# More recursion examples

# powerset - every subset of a list; list of length n will have powerset length 2^n
def powerset(l: list) -> list[list]:
    '''
    return powerset of l
    '''
    if l == []:
        return [[]]
    first, rest = l[0], l[1:]
    lose_it = powerset(rest)
    # Note that you can start with empty set, then prepend each item from the list, then do the same to those, etc.
    use_it = list(map(lambda x:[first]+x, lose_it))
    return use_it + lose_it

# print(powerset([1,2,3]))

def combinations(s,k):
    '''
    return all combinations of set s with length k
    '''
    return list(filter(lambda l: len(l) == k, powerset(s)))

# print(combinations(range(1,6),2))

def combinations_rec(s,k):
    '''
    return all combinations of set s with length k
    '''
    if k == 0:
        return [[]]
    elif k > len(s):
        return []
    first, rest = s[0], s[1:]
    lose_it = combinations_rec(rest,k)
    use_it = list(map(lambda x:[first]+x, combinations_rec(rest, k-1)))
    return use_it + lose_it
# print(combinations_rec(range(1,6),2))