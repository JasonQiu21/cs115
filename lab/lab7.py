####################################################################################
# Name: Jason Qiu
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
####################################################################################


# The binary format you'll be working with for this assignment is called R2L,
# as it is a right-to-left representation.
####################################################################################
## Ex: 8 in decimal is 1000 in standard binary (2^3),
## and represented as a list [0, 0, 0, 1] in our R2L representation.
####################################################################################
from functools import reduce
# Notice that this makes it very easy to work with binary,
# by using num[0] to grab the least significant bit (2^0)!
#
# Please fill out the following 4 functions below using recursion, as specified.

# Given an integer x >= 0, convert it to the R2L binary format.
# Take note that both [] and [0] are used to represent 0 in R2L

def decimalToBinary(x):
   if x == 0:
      return []
   elif x%2 == 0:
      return [0] + decimalToBinary(x//2)
   return [1] + decimalToBinary((x-1)//2)

# Given an R2L formatted number, return the integer it is equivalent to.
# The function should function with both [] and [0] returning 0.
def binaryToDecimal(num):
   if num == [] or num == [0]:
      return 0
   return 2**(len(num)-1) * num[-1] + binaryToDecimal(num[:-1])

# Given an R2L formatted number, return an R2L equivalent to num + 1
# If you need to increase the length, do so. Again, watch out for 0
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

# Given 2 R2L numbers, return their sum.
## You MUST implement recursively the algorithm for bit-by-bit addition as taught in class,
## you may NOT do something like decimalToBinary( binaryToDecimal(num1) + binaryToDecimal(num2) ).
# Make sure to figure out what to do when num1 and num2 aren't of the same length!
# (and be sure you can add [] and [0])
## Tip: Try this on paper before typing it up
def addBinary(num1, num2, carry=0):
   if len(num1) > len(num2):
      return addBinary(num1, num2 + [0])
   elif len(num2) > len(num1):
      return addBinary(num1 + [0], num2)
   elif not(num1 or num2) and carry==1:
      return [1]
   elif not(num1 or num2) and carry==0:
      return []
   elif num1[0] + num2[0] + carry == 3:
      return [1] + addBinary(num1[1:], num2[1:], carry=1)
   elif num1[0] + num2[0] + carry == 2:
      return [0] + addBinary(num1[1:], num2[1:], carry=1)
   elif num1[0] + num2[0] + carry == 1:
      return [1] + addBinary(num1[1:], num2[1:], carry=0)
   return [0] + addBinary(num1[1:], num2[1:], carry=0)