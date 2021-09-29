# practice with (multi-list) map
# functools.reduce
# lambda expressions

# list of squares through map
import math
def squaresList(n: int) -> list[int]:
    '''
    Returns list of squares less than n
    '''
    return list(map(lambda x: x**2, range(math.ceil(math.sqrt(n))))) if n>=0 else []
print(squaresList(100))

def listSum(l1:list, l2:list) -> list:
    '''
    Adds two lists together as if in vector addition.
    '''
    return map(lambda x,y:x+y, l1, l2)