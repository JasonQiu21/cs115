'''
Created on 2021-10-04
@author:   Jason Qiu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 4
'''
import math
def pascal_row(n: int):
    '''
    Return the nth row of Pascal's Triangle; [1] is row 0.
    '''
    def helper(l: list):
        if len(l) <= 1:
            return [1]
        return [l[0]+l[1]] + helper(l[1:])
    if n == 0:
        return [1]
    # elif n == 1:
    #     return [1,1]
    return [1] + helper(pascal_row(n-1))

def pascal_triangle(n, triangle=[]):
    '''
    Return the first n rows of Pascal's Triangle
    '''
    if n == 0:
        return [pascal_row(n)]
    else:
        return pascal_triangle(n-1) + [pascal_row(n)]

def binom(n, k):
    return math.factorial(n) // math.factorial(k) // math.factorial(n - k)
def test_pascal_row():
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1,1]
    assert pascal_row(3) == [1,3,3,1]
    l = []
    for i in range(101):
        l.append(binom(100,i))
    assert pascal_row(100) == l
test_pascal_row()

def test_pascal_triangle():
    assert pascal_triangle(0) == [[1]], f"{pascal_triangle(0)}"
    assert pascal_triangle(1) == [[1],[1,1]], f"{pascal_triangle(1)}"
    assert pascal_triangle(3) == [[1],[1,1],[1,2,1],[1,3,3,1]], f"{pascal_triangle(3)}"
    ll = []
    for i in range(11):
        ll.append(pascal_row(i))
    assert pascal_triangle(10) == ll
test_pascal_triangle()