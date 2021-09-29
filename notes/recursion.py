# To understand recursion, you must first understand recursion.

def fact(n:int) -> int:
    """
    Factorial: n! = n*(n-1)*(n-2)*...*2*1
    """
    # Note that n! = n*(n-1)*(n-2)*...*2*1 = n*(n-1)!
    if n < 0:
        raise Exception("fact() is only defined for nonnegative integers.")
    return 1 if n==0 or n==1 else n*fact(n-1)

def checkPalindrome(s: str) -> bool:
    '''
    Check if a string is a palindrome.
    '''
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    return checkPalindrome(s[1:-1])

palins = []
def palindromes(s: str) -> list[str]:
    '''
    Return all palindromes in a string.
    '''
    global palins
    if len(s) < 1:
        pass
    elif len(s) == 1:
        if s not in palins:
            palins.append(s)
    elif checkPalindrome(s):
        if s not in palins:
            palins.append(s)
        palindromes(s[1:-1])
    else:
        for i in range(1, len(s)):
            palindromes(s[0:i])
            palindromes(s[i:])
    return palins

print(palindromes('geeks'))