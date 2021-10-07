# Stevens Institute of Technology, 2021

##########################################
# Name: Jason Qiu
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
##########################################
from math import floor    # E.g., floor(5.3) -> 5, floor(3.9) -> 3

######################################################################
# Task 1: Given an 8-digit decimal number representing the date,
#         calculate the day of the week using Zeller's congruence:
#
#           https://en.wikipedia.org/wiki/Zeller%27s_congruence
#
# Input:  8-digit decimal number in the format of YYYYMMDD
#
# Output: Weekday as a [0-6] number, where 
#         0: Saturday, 1: Sunday, 2: Monday, ..., 6: Friday  
######################################################################
def getWeekday(date):
    q = date%100
    m = (date%10000)//100
    k = (date//10000)%100
    j = floor((date//10000)/100)
    return (q+floor(13*(m+1)/5+k+floor(k/4)+floor(j/4)-2*j))%7
print(getWeekday(20211007))

######################################################################
# Task 2: Create two functions, an encoder and a decoder for the
#         Caesar cipher:
#
#           https://en.wikipedia.org/wiki/Caesar_cipher
#
# Note: You can try out this cipher at the link below:
#
#           https://cryptii.com/pipes/caesar-cipher
######################################################################

######################################################################
# This provided helper function may be useful
# Input:  List of ASCII values (Ex: [72, 69, 76, 76, 79])
# Output: String (Ex. 'HELLO')       'H   E   L   L   O'
######################################################################
def asciiToString(asciiList):
    return ''.join(map(chr, asciiList))

######################################################################
# Caesar Encoder
#
# Input: A string (assume all-caps: leave everything else as-is),
#        and a shift value       (Ex. 'HELLO WORLD', 3)
#
# Output: An encoded string      (Ex. 'KHOOR ZRUOG')
#
# Hint: The ord() function converts single-character strings to ASCII
#       (Its inverse, the chr() function, is used in the provided helper)
######################################################################
def caesarEncoder(s, shift):
    l = map(ord, s)
    return asciiToString(list(map(lambda x: (x-65+shift)%26+65 if x in range(65, 91) else x,l)))

######################################################################
# Decoder
# Input: A string value with all capital letters (leave everything
#        else as-is) and a shift value (Ex. KHOOR ZRUOG, 3)
# Output: A decoded string             (Ex. HELLO WORLD)
# Hint: The chr() function converts ASCII to a single-character string
######################################################################
def caesarDecoder(s, shift):
    l = map(ord, s)
    return asciiToString(list(map(lambda x: (x-65-shift)%26+65 if x in range(65,91) else x,l)))