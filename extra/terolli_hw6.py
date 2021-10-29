'''
Created on 2021-10-18
@author:   Jason Qiu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

from functools import reduce
def compress(s:str) -> str:
    def helper(s, count=0, counts=[], prev='0'):
        '''
        Returns list of ints corresponding to how many 0's or 1's are in a row; to be converted into binary string later in compress().
        '''
        # print(counts)
        if not s:
            counts.append(count)
            return counts
        elif count >= MAX_RUN_LENGTH:
            counts.append(count)
            count = 0
            prev = '0' if prev == '1' else '1'
            return helper(s, count, counts, prev)
        elif s[0] != prev:
            counts.append(count)
            count = 0
            prev = s[0]
            return helper(s, count, counts, prev)
        elif s[0] == prev:
            count +=1
        return helper(s[1:], count, counts, prev) if len(s) > 1 else helper('', count, counts, prev)
        
    
    def decimalToBinary(x):
        if x == 0:
            return '' 
        elif x%2 == 0:
            return decimalToBinary(x//2) + '0'
        return decimalToBinary((x-1)//2) + '1'
    def pad(x, l=COMPRESSED_BLOCK_SIZE):
        if len(x) >= l:
            return x
        return pad('0' + x)
    a = helper(s)
    # print(a)
    c = reduce(lambda x,y: x+y, map(lambda x: pad(decimalToBinary(x)), a))
    return c

def uncompress(s:str, switch='0') -> str:
    def binaryToNum(s):
        if s=="":
            return 0
        elif s[0]=="1":
            return 1*2**(len(s)-1)+binaryToNum(s[1:])
        else:
            return binaryToNum(s[1:])
    def helper(s):
        '''
        Returns list of ints from binary string encoded as per compress()
        '''
        if not s:
            return []
        return [binaryToNum(s[0:COMPRESSED_BLOCK_SIZE])] + helper(s[5:])
    a = helper(s)
    return reduce(lambda x,y: x+y, map(lambda x,y: '0'*x if y%2 == 0 else '1'*x, a, range(len(a))))

def compression(s):
    return len(compress(s))/len(s)

# penguin = '00011000' + '00111100'*3 + '01111110' + '11111111' + '00111100' + '00100100'

# print(compress(penguin))
# assert uncompress(compress(penguin)) == penguin
# print(compression(penguin))

# sequence = '1' * MAX_RUN_LENGTH + '0' * MAX_RUN_LENGTH + '1' * (64 - 2 * MAX_RUN_LENGTH)
# print(sequence)
# print(compress(sequence))



# Prof. Lai is wrong. Say Prof. Lai's function compresses a binary number of length N into length N-x. For all values of x less N, 
# the 2^N different cases cannot be represented by the set of 2^(N-x) compressed cases. Different length compressed numbers
# would require the use of digits that are not 1 or 0.