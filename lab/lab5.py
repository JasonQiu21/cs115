# Lab 5 -- done Wed, 2021-09-29
#
#
# I pledge my honor that I have abided by the Stevens Honor System.
# Jason Qiu
def dotProduct(l: list[float], k: list[float]) -> list[float]:
    '''
    Vector dot product l*k: l1*k1+l2*k2*...*lx*kx
    ''' 
    if len(l) != len(k):
        raise Exception("l and k have to be the same length.")
    elif l == [] and k == []:
        return 0
    return l[0]*k[0] + dotProduct(l[1:], k[1:])
# assert dotProduct([5,3], [6,4]) == 42
def removeAll(e, l:list) -> list:
    '''
    Remove all elements of list l that are element e
    '''
    if l == []:
        return []
    elif l[0] == e:
        return removeAll(e, l[1:])
    return [l[0]] + removeAll(e, l[1:])
# assert removeAll(42, [ 55, 77, 42, 11, 42, 88 ]) == [ 55, 77, 11, 88 ] 
# assert removeAll(42, [ 55, [77, 42], [11, 42], 88 ]) == [ 55, [77, 42], [11, 42], 88 ]

def geometricSeq(n: int,f: float, b: float) -> float:
    '''
    Geometric sequence computed by a(n) = f×a(n-1) for all n >= 1
    '''
    if f == 0 or b == 0:
        raise Exception("base and multiplicative factor of geometric sequence cannot be 0.")
    if n == 1:
        return b
    return f*geometricSeq(n-1,f,b)
# assert geometricSeq(1, 2, 5) == 5
# assert geometricSeq(3, 3, 1) == 9
# assert geometricSeq(3, 2, 10) == 40

def deepReverse(l) -> list:
    '''
    Reverse list l and any lists inside of it (and inside of them, and so on)
    '''
    if not isinstance(l, list):
        return l
    elif l == []:
        return []
    return [deepReverse(l[-1])] + deepReverse(l[:-1])
# assert deepReverse([1, 2, 3]) == [3,2,1]
# assert deepReverse([1, [2, 3], 4]) == [4,[3,2],1]
# assert deepReverse([1, [2, [3, 4], [5, [6, 7], 8]]]) == [[[8, [7, 6], 5], [4, 3], 2], 1]