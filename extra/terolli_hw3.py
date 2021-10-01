'''
Created on 2021-10-01
@author:   Jason Qiu
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# your code goes here

# function change() from lab 3-1
def change(a: int, coins = [1,5,10,25,50]):
    '''
    Give number of coins to make change for amount a
    '''
    if coins == []:
        return float('inf')
    elif a == coins[-1]:
        return 1
    elif a <= coins[-1]:
        return change(a, coins[:-1])
    use_it = 1 + change(a-coins[-1], coins)
    lose_it = change(a, coins[:-1])
    return min(use_it, lose_it)
# print(change(48, [1, 5, 10, 25, 50]))
# print(change(48, [1, 7, 24, 42]))

def giveChange(a: int, coins = [1,5,10,25,50]):
    '''
    Give change in coins for amount a. Returns number of coins, then list of coin values
    '''
    def helper(a, coins, b = True):
        if coins == []:
            return []
        elif a == coins[-1]:
            return [coins[-1]]
        elif a <= coins[-1]:
            return helper(a, coins[:-1])
        use_it = [coins[-1]] + helper(a-coins[-1], coins)
        lose_it = helper(a, coins[:-1])
        return lose_it if len(lose_it) < len(use_it) and lose_it!=[] else use_it
    return [change(a, coins), helper(a, coins)]
# print(giveChange(48, [1, 5, 10, 25, 50]))
# print(giveChange(48, [1, 7, 24, 42]))
# print(giveChange(35, [1, 3, 16, 30, 50]))


# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    if dct == []:
        return []
    def letterToNumber(a, i=0):
        if len(a) != 1:
            raise Exception("a must be a single letter")
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        return i if letters[i]==a else letterToNumber(a, i+1)
    def score(word, scores=scores):
        if word == '':
            return 0
        return scores[letterToNumber(word[0].lower())][1] + score(word[1:], scores)
    
    return [dct[0], score(dct[0])] + wordsWithScore(dct[1:], scores)

# print(wordsWithScore(Dictionary, scrabbleScores))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
' (Notice that you cannot assume anything about the length of the list.)
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n], assuming L is a list and n is at least 0.'''
    if n==0:
        return []
    return [L[0]] + take(n-1, L[1:])
# assert take(3, [1,2,3,4,5,6]) == [1,2,3,4,5,6][0:3], f"{take(3, [1,2,3,4,5,6])}    {[1,2,3,4,5,6][0:3]}"

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:], assuming L is a list and n is at least 0.'''
    if n==0:
        return L
    return drop(n-1,L[1:])
# assert drop(3, [1,2,3,4,5,6]) == [1,2,3,4,5,6][3:], f"{drop(3, [1,2,3,4,5,6])}    {[1,2,3,4,5,6][3:]}"