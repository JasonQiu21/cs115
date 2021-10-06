####################################################################################
# Name: Jason Qiu
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
####################################################################################
# Lab 6: Recursion 2
# Demonstrate recursion as an algorithm design technique for the problem of 
# computing the (length of the) longest common subsequence of two given strings
#
# Note: Using anything other than recursion will result in a penalty
#####################################################################################

##############################################################################
# Example: The longest common subsequence of "helllowo_rld" and "!helloabcworld!"
# is "helloworld", and it has a length of 10.
#
# Therefore LLCS("helllowo_rld", "!helloabcworld!") returns 10, and
# LCS("helllowo_rld", "!helloabcworld!") returns "helloworld"
##############################################################################
def helper(a, b,i=0):
    '''
    Find element in b that matches a
    '''
    if len(a) != 1:
        raise Exception("length of a must be 1")
    if a == b[i]:
        return i
    return helper(a, b, i+1)
def myLen(a):
    '''
    Equivalent of len()
    '''
    if not a:
        return 0
    return 1 + myLen(a[1:])
def myMax(a, b):
    '''
    Return the max of a or b if a and b are numbers; else, return the element with longer length
    '''
    if isinstance(a, int) or isinstance(b, int):
        return a if a>b else b
    return a if myLen(a) > myLen(b) else b
    
def LLCS(S1, S2):
    '''
    Return the length of the longest common subsequence (LLCS) of strings S1 and S2; equivalent to len(LCS(S1, S2))
    '''
    
    if not S1 or not S2:
        return 0
    if S1[0] in S2:
        index = helper(S1[0], S2)
        if index+1 == myLen(S2):
            use_it = 1 + LLCS(S1[1:], S2[-1])
        elif index == myLen(S2):
            use_it =  1 +LLCS(S1[1:], "")
        else:
            use_it = 1 + LLCS(S1[1:], S2[index+1:])
        lose_it = LLCS(S1[1:], S2)
        return myMax(use_it, lose_it)
    return LLCS(S1[1:], S2)

# assert LLCS("helllowo_rld", "!helloabcworld!") == 10, LLCS("helllowo_rld", "!helloabcworld!")
##############################################################################
# Instead of returning the length of the longest common substring, this task
# asks you to return the string itself.
##############################################################################
# Tip: You may find it helpful to copy your solution to LLCS and edit it
# to solve this problem
##############################################################################

def LCS(S1, S2):
    '''
    Return the longest common subsequence (LCS) between strings S1 and S2
    '''
    if not S1 or not S2:
        return ""
    if S1[0] in S2:
        index = helper(S1[0], S2)
        if index+1 == myLen(S2):
            use_it = S1[0] + LCS(S1[1:], S2[-1])
        elif index == myLen(S2):
            use_it =  S1[0] +LCS(S1[1:], "")
        else:
            use_it = S1[0] + LCS(S1[1:], S2[index+1:])
        lose_it = LCS(S1[1:], S2)
        return myMax(use_it, lose_it)
    return LCS(S1[1:], S2)
# assert LCS("helllowo_rld", "!helloabcworld!") == "helloworld", LCS("helllowo_rld", "!helloabcworld!")
# assert len(LCS("helllowo_rld", "!helloabcworld!")) == LLCS("helllowo_rld", "!helloabcworld!")