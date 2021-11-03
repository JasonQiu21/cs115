# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Name    : Jason Qiu
# Pledge  : I pledge my honor that I have abided by the Stevens Honor System.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Max:
#  Write a hmmm function that gets two numbers,
#   then prints the larger of the two.
#  Assumptions: Both inputs are any integers
Max = """
# Input: n,m
# Output: n if n>m else m
# Assume: n,m are ints
00 read r1          # Get n
01 read r2          # Get m
02 sub r3 r2 r1     # r3 = r2-r1
03 jgtzn r3 06      # if r3>0, jump to 06
04 write r1         # print r1
05 halt
06 write r2         # print r2
07 halt
"""


# Power:
#  Write a hmmm function that gets two numbers,
#   then prints (No.1 ^ No.2).
#  Assumptions: No.1 is any integer, No.2 >= 0
Power = """
# Input: n,m
# Output: n^m
# Assume: m>=0; n,m are ints
00 read r1      # Get n
01 read r2      # Get m
02 setn r3 1    # Initialize r3
03 jeqzn r2 07  # If exp==0, jump line 7
04 mul r3 r1 r3 # r3*=r1
05 addn r2 -1   # r2--
06 jumpn 03     # repeat
07 write r3     # print r3
08 halt
"""


# Fibonacci
#  Write a hmmm function that gets one number,
#   then prints the No.1st fibonacci number.
#  Assumptions: No.1 >= 0
#  Tests: f(2) = 1
#         f(5) = 5
#         f(9) = 34
Fibonacci = """
# Input: n
# Output: nth Fibbonacci number; f(0) = 1
# Assume: n>=0; n is an int
00 read r1          # Get n
01 setn r2 1        # init r2,r3,r4
02 setn r3 1        # ^
03 setn r4 1        # ^
04 copy r5 r2       # set r5 to r2
05 jeqzn r1 12      # done if r1 is 0
06 copy r5 r2       # set r5 to r2
07 copy r4 r2       # r4 gets set to r2
08 copy r2 r3       # r2 gets set to r3
09 add r3 r2 r4     # r3 = r2 + r4
10 addn r1 -1       # r1--
11 jumpn 05         # repeat
12 write r5         # print r5
13 halt
"""


# ~~~~~ Running ~~~~~~
import hmmm
import importlib

runThis = Max  # Change to the function you want to run
doDebug = True # Change to turn debug mode on/off

# call main() from the command line to run the program again
def main(runArg = runThis, debugArg = doDebug):
    importlib.reload(hmmm)
    hmmm.main(runArg, debugArg)

if __name__ == "__main__" : 
    main()
