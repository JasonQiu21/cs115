'''
Created on 10/14/2021
@author:   Jason Qiu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return True if n%2 == 1 else False
    
    #Number 42 is 101010 in binary
    
    #If I am given an odd base-10 number, the rightmost bit will be 1 in base-2
    #If I am given an even base-10 number, the rightmost bit will be 0 in base-2
    
    #By eliminating the least-significant bit, the base-2 number is getting divided by 2 with integer division

    #If N is odd, we will put a 1 in the rightmost bit in base-2 and then do integer division to N
    #If N is even, we will put a 0 in the rightmost bit in base-2 and then do integer divison
    #By continuously doing these two steps until Y=0, we get the base-2 number
    
def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n==0:
        return ""
    elif n%2==0:
        return numToBinary(n>>1)+"0"
    else:
        return numToBinary(n>>1)+"1"

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s=="":
        return 0
    elif s[0]=="1":
        return 1*2**(len(s)-1)+binaryToNum(s[1:])
    else:
        return binaryToNum(s[1:])
def incrementBinary(num, carry=1):
   if carry == 1:
      if num == []:
         return [1]
      elif num[0] == 1:
         return [0] + incrementBinary(num[1:],carry=1)
      return [1] + incrementBinary(num[1:],carry=0)
   if num == []:
      return []
   elif num[0] == 1:
      return [1] + incrementBinary(num[1:],carry=0)
   return [0] + incrementBinary(num[1:],carry=0)

def increment(s, carry=1):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if s=='11111111':
        return '00000000'
    if carry == 1:
        if not s:
            return '1'
        elif s[-1] == '1':
            return increment(s[:-1], 1) + '0'
        return increment(s[:-1], 0) + '1'
    if not s:
        return ''
    return increment(s[:-1], 0) + s[-1]
def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n==0:
        print(s)
    else:
        print(s)
        s=increment(s)
        return count(s,n-1)
count('00010000', 4)
#The number 59 is 2012 in base-3

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n==0:
        return ""
    return numToTernary(n//3) + str(n%3)
def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if len(s) == 0:
        return 0
    return int(s[-1]) + 3*(ternaryToNum(s[:-1]))