# I pledge my honor that I have abided by the Stevens Honor System.
#
# 
# Jason Qiu
# 2021-11-14

from importlib import reload as Rfrsh
import hmmm

# Fibonacci! You've already done it in Lab 9
# Now however, you are to do hmmmonacci with
# recursion, & you MUST do so for any credit
# The tests are still the same as from Lab 9
# Tests: f(2) = 1, f(5) = 5, f(9) = 34
RecFibSeq = """
# Input: n
# Output: nth Fibbonacci number; f(0) = 1
# Assume: n>=0; n is an int
00 setn r15 42      # Set stack pointer
01 setn r2 2
02 read r1
03 calln r14 06     # Initial function call
04 write r13
05 halt

06 sub r3 r1 r2
07 jgtzn r3 11
08 setn r13 1
09 setn r12 1
10 jumpr r14

11 pushr r1 r15     # Recursive function call 1 (fib(n-2))
12 pushr r14 r15
13 addn r1 -2
14 calln r14 06
15 popr r14 r15
16 popr r1 r15

17 pushr r1 r15     # Recursive function call 2 (fib(n-1))
18 pushr r14 r15
19 addn r1 -1
20 calln r14 06
21 popr r14 r15
22 popr r1 r15

23 pushr r13 r15
24 add r13 r13 r12
25 popr r12 r15
26 jumpr r14
"""

# Change doDebug to false to turn off debugs
runThis = RecFibSeq
doDebug = True

# Note: main() in the shell to easily reload
def main(runArg=runThis,  debugArg=doDebug):
    Rfrsh(hmmm); hmmm.main(runArg, debugArg)

if __name__ == "__main__" :
    main()
