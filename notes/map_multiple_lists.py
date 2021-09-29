# Multi-iterable map funciton

lst = [4,1,3,5,7,8,6,9]
def avgList(l: list[int]) -> list[int]:
    '''
    Returns list where each middle element is the average of itself, its predecessor, and its successor in l.
    '''
    if len(l)<3:
        return l
    mid = list(map(lambda a,b,c:(a+b+c)//3, l[1:-1], l[:-2], l[2:]))
    mid.insert(0, l[0])
    mid.append(l[-1])
    return mid

print(avgList(lst))