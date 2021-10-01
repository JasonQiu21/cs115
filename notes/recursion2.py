# Notes 2021-10-01
# More recursion examples, esp. with lists; use it/lose it concept


# General form of a tail-end recursive function on a list
# def recursive_list_function(L):
#         base_val = ...
#         def recursive_step(h,t):
#             ...
#         if L == []: # Alternatively, if not L
#             result = base_val
#         else:
#             head, tail = L[...], L[...]
#             result = recurseive_step(head, tail)
#         return result

def recursive_deep_len(l):
    '''
    Returns number of elements in a list, counting elements of lists in the list.
    '''
    base_val = 0
    def recursive_step(h,t):
        if type(h) != list:
            head_contribution = 1
        else:
            head_contribution = recursive_deep_len(h)
        tail_contribution = recursive_deep_len(t)
        return head_contribution + tail_contribution
    if l == []:
        return base_val
    return recursive_step(l[0], l[1:])
assert recursive_deep_len([[1,2],3,4]) == 4
assert recursive_deep_len([[],[[[],[],]],[[[[],[]]]]]) == 0

def recursive_map(f, l):
    '''
    Recursive version of map function for a single list.
    Returns the same as map(f,l)
    '''
    if l == []:
        return []
    return [f(l[0])] + recursive_map(f, l[1:])
assert recursive_map(lambda x: 2*x,  [1,2,3,4]) == [2,4,6,8]

# Branch recursion - use it or lose it
# count combinations
# choose

def choose(n,k):
    '''
    count the number of ways that k distinct items might be chosen from a group of n
    '''
    if n<k:
        raise Exception("k must be less than or equal to n")
    elif n<0 or k<0 or type(n)!=int or type(k)!=int:
        raise Exception("n and k must be positive integers")
    elif k==0 or k==n:
        return 1
    else:
        # Use first item -> k-1 things to pick out of n-1
        # Lose first item -> k things to pick out of n-1
        use_it = choose(n-1,k-1)
        lose_it = choose(n-1,k)
        return use_it + lose_it
assert(choose(3,0)) == 1
assert(choose(3,1)) == 3
assert(choose(5,3)) == 10