# Some reduce review
from functools import reduce

def getMax(l:list[int]) -> int:
    '''
    return max value in list; equivalent to built-in max()
    '''
    return reduce(lambda x,y: x if x>y else y, l)

# filter(function, iterable) - function returns boolean (or other format convertable to boolean, e.g. returning 1 or 0, 
# and keeps elements of the iterable if the function returns true for that element.
def evens(b:int) -> list[int]:
    '''
    Return all even numbers until bound b
    '''
    return list(filter(lambda x:x%2==0, range(b)))

def mults(b: int,n: int) -> list[int]:
    '''
    Return all multiples of n until bound b
    '''
    return list(filter(lambda x:x%n==0, range(b)))