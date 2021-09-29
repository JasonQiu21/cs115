l = [1,2,3,4,5] # This is a lsit
print(l[0]) # First item in l; lists index from 0 in most languages (save for R, Matlab, a few others)

l[2] = 9 # Changes the 3rd element in a list to 9
print(l)

l2 = ['a', 'b', 'c']
print(l2)

# List addision concatenates the second list to the first. 
# Concatenating a list of ints and strs is posisble in Python because of the nature of the language.
print(l + l2) 

# Lists in lists
l3 = [l,l2,"Hello", "World"]
print(l3)
print(len(l3))
print(l3[0][2])

# Slicing lists; when slicing, position 0 is before the first number. Negatives work too.
# a[start:stop]  items start through stop-1
# a[start:]      items start through the rest of the array
# a[:stop]       items from the beginning through stop-1
# a[:]           a copy of the whole array
# a[start:stop:step] start through not past stop, by step
# a[::-1]    all items in the array, reversed
# a[1::-1]   the first two items, reversed
# a[:-3:-1]  the last two items, reversed
# a[-3::-1]  everything except the last two items, reversed
# all of this is equivalent to using slice(start, stop, step); slice accepts None type as well, just like :
print(l[2:5])
# First 2 values
print(l[:2])
# Last 2 values
print(l[-2:])

# Map function maps a function onto an iterable; another way to iterate without the use of loops

# Synatx: map(function, iterable)
# Returns object map; wrap in list() to create list
import math
def isPrime(n):
    return not 0 in map(lambda x:n%x, range(2,math.ceil(n**0.5)+1))

print(isPrime(37))